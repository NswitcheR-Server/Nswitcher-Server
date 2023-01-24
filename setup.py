from distutils.core import setup

from setuptools import find_packages

install_requires = [
	'eventlet~=0.30.0',
	'joycontrol @ git+https://github.com/mart1nro/joycontrol.git@721646a7ec10231490bcf788b3bdde10d8c2007f',
	'flask-socketio~=5.0.0',
]

test_deps = [
	'pytest',
]

setup(
	name='nswitcher-server',
	version='1.0.0',
	packages=find_packages(),
	license='MIT',
	author="Titimousse, AntoLeGololo",
	author_email='',
	description="Remote play Nintendo NS without hack.",
	install_requires=install_requires,
	tests_require=test_deps,
	extras_require=dict(
			test=test_deps,
	),
)
