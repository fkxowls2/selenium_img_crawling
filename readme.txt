python version 3.8

UI디자인 프로그램 실행 명령어
$ designer

실행파일 생성 명령어
$ pyinstaller -w -F main.py
실행파일 생성되면 실행파일을 dist폴더에서 현재 폴더로 이동
이후 실행파일, lotto.ui, lotto.pkl(없으면 생성하지만 오래걸림)만 있으면 파일 실행 가능

실행파일에서 셀레니움 실행시에 콘솔창 뜨는 문제 해결
- 빌드전에 라이브러리 Lib\site-packages\selenium\webdriver\common\service.py 열어서
  self.process = subprocess.Popen(cmd, env=self.env,
  close_fds=platform.system() != 'Windows',
  stdout=self.log_file,
  stderr=self.log_file,
  stdin=PIPE)
에 마지막(PIPE 다음)에 creationflags=0x08000000 입력