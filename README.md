
# CodeAgent

## Full version of source codes, 
please visit: https://zenodo.org/records/11666403

## Source Code
please visit: https://zenodo.org/records/10607925

## Overview

CodeAgent is a project aimed at demonstrating language-specific functionalities and logging activities for educational or research purposes. This repository contains various scripts and data files organized by programming languages and logs of online activities.

## Repository Structure

```
CodeAgent/
├── EMNLP-CodeAgent 2/
│   ├── Languages/
│   │   ├── c/
│   │   ├── c#/
│   │   ├── c++/
│   │   ├── go/
│   │   ├── java/
│   │   ├── javascript/
│   │   ├── php/
│   │   ├── python/
│   │   └── ruby/
│   ├── online_log/
│   │   ├── static/
│   │   │   ├── avatars/
│   │   │   ├── replay/
│   │   │   │   ├── css/
│   │   │   │   └── js/
│   │   │   └── other files
│   └── ScriptTest/
│       ├── top_Perl_repos.json
│       ├── codeagent_data.py
│       ├── config.json
│       └── codeagent.log
└── __MACOSX/
```

### Languages
This directory contains folders for various programming languages. Each folder includes scripts and examples written in the respective language.

### online_log
This directory contains logs of online activities, including static assets such as avatars and replay files.

### ScriptTest
This directory contains scripts and data for testing purposes, including a configuration file, a Python data script, and a log file.

## Setup

Before running the scripts, ensure you have the required environment and dependencies set up.

1. **Activate Conda Environment**:
   ```bash
   conda activate ChatDev_conda_env
   ```

2. **Set OpenAI API Key**:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

Replace `"your_openai_api_key"` with your actual OpenAI API key.

## Usage

### Example Command

To run a script with specific parameters, you can use the following command. This example is shown in `runcopy.sh`.

```bash
python3 run.py --ifcode "commit" --name "eccl-codereview" --commit "Diff-CodeAgent4.0/6e3c6d17d943f5ac70b421653eb167e0c34b119f-commit.txt" --commitmessage "Diff-CodeAgent4.0/6e3c6d17d943f5ac70b421653eb167e0c34b119f-message.txt" --originalfile "Diff-CodeAgent4.0/6e3c6d17d943f5ac70b421653eb167e0c34b119f-context.txt"
```

### Parameters

- `--ifcode`: Specifies the operation type. In this case, "commit".
- `--name`: Name of the operation or task.
- `--commit`: Path to the commit file.
- `--commitmessage`: Path to the commit message file.
- `--originalfile`: Path to the original file for context.

## Requirements

To run the Python scripts in the `ScriptTest` directory, you need Python installed on your system. Other languages have their respective requirements.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
