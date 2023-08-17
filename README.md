# Tebis Problem

## Cloning

Clone the repo:

```bash
git clone --depth 1 https://github.com/renjeik/tebis.git
```

## (Optional) Anaconda setup

If you need multiple python version in your local machine, you can setup a virtual environment for each version.

The enviroment that we are going to use throughout this project is Anaconda.

Download and install it conda, from https://www.anaconda.com/.

Open Anaconda Prompt/Terminal and create an environment using the command:

```bash
conda create --name <NAME OF ENVIRONMENT> python=3.11.4 -y
```

Next, activate the environment using the command:

```bash
conda activate <NAME OF ENVIRONMENT>
```

You will notice that the name of the current activated name is shown in the command line, like:

```bash
(<NAME OF ENVIRONMENT>) current/working/directory>
```

Make sure to check the name of the environment everytime you run a command in a terminal.

## Setup

To run an app, simply run:

```bash
python triangle.py <FILE TEXTNAME>.txt
```
