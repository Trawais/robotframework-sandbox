import platform
import subprocess
from pathlib import Path
from venv import EnvBuilder

venv_dir = Path(".") / ".venv"
if not platform.platform().startswith("Windows"):
    venv_python = venv_dir / "bin" / "python"
else:
    venv_python = venv_dir / "Scripts" / "python.exe"

if not venv_dir.exists():
    print(f"Creating virtualenv in {venv_dir}")
    EnvBuilder(with_pip=True).create(venv_dir)

subprocess.run([venv_python, "-m", "pip", "install", "-U", "pip"])
subprocess.run([venv_python, "-m", "pip", "install", "-U", "-r", "requirements.txt"])
subprocess.run([venv_python, "-m", "Browser.entry", "init", "chromium"])

activate_script = (
    "source .venv/bin/activate"
    if not platform.platform().startswith("Windows")
    else ".venv\\Scripts\\activate"
)
print(f"Virtualenv `{venv_dir}` is ready and up-to-date.")
print(f"Run `{activate_script}` to activate the virtualenv.")
