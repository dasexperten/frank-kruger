import contextlib
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace as Args
import unittest

spec = importlib.util.spec_from_file_location('memory', Path(__file__).resolve().parents[1] / 'tools/memory.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old = m.ROOT
        m.ROOT = Path(self.tmp.name)
        (m.ROOT / 'research').mkdir()
        self.source = m.ROOT / 'research/source.md'
        self.source.write_text('Инвестиционная готовность\nHypothesis is not a result.\nDCF evidence\n', encoding='utf-8')

    def tearDown(self):
        m.ROOT = self.old
        self.tmp.cleanup()

    def call(self, fn, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            fn(*args)
        return out.getvalue()

    def candidate(self, id='one', review_on=None):
        self.call(m.propose, Args(id=id, claim='Source states a hypothesis', scope='document only',
            source='research/source.md', start=1, end=2, kind='fact', review_on=review_on))

    def transition(self, id='one', status='active', replacement=None):
        self.call(m.transition, Args(id=id, status=status, replacement=replacement,
                  reviewer='test reviewer', reason='synthetic fixture evidence checked'))

    def groups(self):
        m.build()
        self.call(m.cycle)
        return m.read_json('indexes/memory.json')['groups']

    def test_candidate_never_usable_and_activation(self):
        self.candidate()
        self.assertEqual(self.groups()['usable'], [])
        self.transition()
        self.assertEqual(self.groups()['usable'], ['one'])

    def test_changed_or_deleted_evidence_is_not_usable(self):
        self.candidate(); self.transition()
        self.source.write_text('Changed claim\n', encoding='utf-8')
        self.assertEqual(self.groups()['review_due'], ['one'])
        self.source.unlink()
        self.assertEqual(self.groups()['usable'], [])

    def test_expired_cannot_activate(self):
        self.candidate(review_on=dt.date.today().isoformat())
        with self.assertRaises(ValueError):
            self.transition()

    def test_dispute_supersede_and_history(self):
        self.candidate(); self.transition(); self.transition(status='disputed')
        self.assertEqual(self.groups()['usable'], [])
        with self.assertRaises(ValueError):
            self.transition(status='superseded', replacement='missing')
        self.candidate('two'); self.transition('two')
        self.transition(status='superseded', replacement='two')
        self.assertEqual(self.groups()['usable'], ['two'])
        self.assertEqual(self.groups()['history'], ['one'])
        self.assertEqual(len(m.read_json(m.CARDS)[0]['events']), 3)
        with self.assertRaises(ValueError):
            self.transition()

    def test_retrieval_unicode_budget_and_refresh(self):
        args = Args(query='готовность', limit=3, budget=200)
        found = json.loads(self.call(m.search, args))
        self.assertEqual(found['evidence'][0]['path'], 'research/source.md')
        self.assertLessEqual(found['characters'], 200)
        self.source.write_text('Совсем другой материал\n', encoding='utf-8')
        self.assertEqual(json.loads(self.call(m.search, args))['evidence'], [])
        self.assertEqual(json.loads(self.call(m.search, Args(query='материал',limit=1,budget=1)))['evidence'], [])

    def test_path_escape_symlinks_and_exclusions(self):
        for path in ('../outside.txt', '/etc/passwd'):
            with self.assertRaises(ValueError):
                m.safe_file(path)
        (m.ROOT / 'research/link.md').symlink_to(self.source)
        (m.ROOT / '.env').write_text('SECRET')
        (m.ROOT / 'research/code.py').write_text('not indexed')
        self.assertEqual(list(m.sources()), ['research/source.md'])
        with self.assertRaises(ValueError):
            m.safe_file('research/link.md')

    def test_invalid_lines_and_duplicate_id(self):
        with self.assertRaises(ValueError):
            m.evidence('research/source.md', 0, 2)
        self.candidate()
        with self.assertRaises(ValueError):
            self.candidate()

if __name__ == '__main__':
    unittest.main()
