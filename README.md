# Tank Controller in Python

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Project Motivations

Update the `TankController` code from C++ to Python and run on a Raspberry Pico.

# Getting Started

## Requirements

Before running the project, install the following:

- **Python 3.14+**
- **uv** (Python package manager)
  - Installation: https://docs.astral.sh/uv/
- **Tkinter** (required for the local GUI)
  - Verify the installation:

    ```bash
    python -m tkinter
    ```

    A small GUI window should appear if Tkinter is installed correctly.

### macOS

Older Python versions may have issues running the GUI. Install Tkinter for Python 3.14:

```bash
brew install python-tk@3.14
```

### Windows

Windows development requires **Windows Subsystem for Linux (WSL)**.

#### 1. Install WSL

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

Restart your computer, open **Ubuntu**, and create your Linux username and password.

Update Ubuntu:

```bash
sudo apt update
sudo apt upgrade -y
```

#### 2. Install Development Tools

```bash
sudo apt install git python3 python3-pip python3-venv build-essential
```

Install **uv**:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reload your shell:

```bash
source ~/.bashrc
```

## Clone the Repository

From your Ubuntu terminal:

```bash
cd ~
git clone https://github.com/username/TankControllerPico.git
cd TankControllerPico
```

## Open in VS Code (Windows)

1. Install the **Remote - WSL** extension.
2. Open the project from the Ubuntu terminal:

```bash
code .
```

Install the **Python** and **Pylance** extensions in **WSL: Ubuntu**.

## Set Up the Python Environment

Create a virtual environment and install the project dependencies:

```bash
uv venv
uv pip install -e ".[dev]"
```

## Run the Project

Launch the local GUI with mocked devices:

```bash
./run_gui.sh
```

## picture

Running the project should launch the TankController GUI.

<p align="center">
  <img src="images/gui_screenshot.png" alt="TankController GUI" width="800">
</p>


## Features

| View Commands    | Set Commands     |
| ---------------- | ---------------- |
| View IP and MAC  | pH calibration   |
| View free memory | Clear pH calibra |
| View Google mins | Clear Temp calib |
| View log file    | Set chill/heat   |
| View pH slope    | Set Google mins  |
| View PID         | Set KD           |
| View tank ID     | Set KI           |
| View temp cal    | Set KP           |
| View time        | Set pH target    |
| View version     | Set pH w sine    |
|                  | Set Temp w sine  |
|                  | PID on/off       |
|                  | Set Tank ID      |
|                  | Temp calibration |
|                  | Set temperature  |
|                  | Set date/time    |

## Testing

To perform Pytest tests for the devices and UI states.

```sh
./test.sh
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/kadensukachevin/"><img src="https://avatars.githubusercontent.com/u/26241731?v=4?s=100" width="100px;" alt="Kaden Sukachevin"/><br /><sub><b>Kaden Sukachevin</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=kadensu" title="Code">💻</a> <a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=kadensu" title="Documentation">📖</a> <a href="https://github.com/Open-Acidification/TankControllerPico/issues?q=author%3Akadensu" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/prestoncarman"><img src="https://avatars.githubusercontent.com/u/3517157?v=4?s=100" width="100px;" alt="Preston Carman"/><br /><sub><b>Preston Carman</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=prestoncarman" title="Code">💻</a> <a href="https://github.com/Open-Acidification/TankControllerPico/issues?q=author%3Aprestoncarman" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/KonradMcClure"><img src="https://avatars.githubusercontent.com/u/66455502?v=4?s=100" width="100px;" alt="Konrad McClure"/><br /><sub><b>Konrad McClure</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=KonradMcClure" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Noah-Griffith"><img src="https://avatars.githubusercontent.com/u/78978886?v=4?s=100" width="100px;" alt="Noah-Griffith"/><br /><sub><b>Noah-Griffith</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=Noah-Griffith" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/d-cryptic"><img src="https://avatars.githubusercontent.com/u/52271502?v=4?s=100" width="100px;" alt="Barun Debnath"/><br /><sub><b>Barun Debnath</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=d-cryptic" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://kieransukachevin.github.io/first%20portfolio/portfolio.html"><img src="https://avatars.githubusercontent.com/u/54186484?v=4?s=100" width="100px;" alt="Kieran Sukachevin"/><br /><sub><b>Kieran Sukachevin</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=kieransukachevin" title="Tests">⚠️</a> <a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=kieransukachevin" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jsoref"><img src="https://avatars.githubusercontent.com/u/2119212?v=4?s=100" width="100px;" alt="Josh Soref"/><br /><sub><b>Josh Soref</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=jsoref" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/TaylorSmith28"><img src="https://avatars.githubusercontent.com/u/83837157?v=4?s=100" width="100px;" alt="TaylorSmith28"/><br /><sub><b>TaylorSmith28</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=TaylorSmith28" title="Tests">⚠️</a> <a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=TaylorSmith28" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/samuelnguyen999"><img src="https://avatars.githubusercontent.com/u/57112921?v=4?s=100" width="100px;" alt="Samuel Nguyen"/><br /><sub><b>Samuel Nguyen</b></sub></a><br /><a href="https://github.com/Open-Acidification/TankControllerPico/commits?author=samuelnguyen999" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
