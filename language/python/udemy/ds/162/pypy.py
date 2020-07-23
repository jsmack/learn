# pip3 install pytest-cov pytest-xdist
#  pytest pypy.py  --cov=calculation --cov-report term-missing
import calculation
import pytest
import os

is_release = True
class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'
        cls.test_dir = '/tmp/test_dir'

    def test_save_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir,self.test_file_name)
        assert os.path.exists(test_file_path) is True
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)


    def setup_method(self,method):
        print('setup method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self,method):
        print('tear method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self, tmpdir):
        print('tmpdir={}'.format(tmpdir))

    def test_save(self,tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

    #@pytest.mark.skip(reason='skip')
    def test_add_add_num_and_double(self,request):
        os_name = request.config.getoption('--os-name')
        print('os-name={}'.format(os_name))
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    @pytest.mark.skipif(is_release==False,
                        reason='skip!')
    def test_add_num_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1','1')


    def test_csv_file(self,csv_file):
        print(csv_file)
        csv_file.write('test')
        assert self.cal.add_num_and_double(1, 1) == 4

