# Personalized Email Generator

This project is a personalized email generator that customizes template emails for recipients using their information. The application reads recipient details from a CSV file, personalizes the email content, and saves the personalized emails as text files.

## Features
- Personalizes emails based on recipient details such as name, email, bio, and last conversation.
- Revises draft emails to match a specified writing style.
- Uses advanced AI models to achieve high-quality personalization.

## Setup and Installation

### Prerequisites
- Anaconda or Miniconda
- Python 3.10

### Steps to Setup the Environment

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/personalized-email-generator.git
   cd personalized-email-generator
   ```

2. **Create a new conda environment**
   ```sh
   conda create -n email_gen python=3.10
   ```

3. **Activate the environment**
   ```sh
   conda activate email_gen
   ```

4. **Install required packages**
   ```sh
   pip install -r requirements.txt
   ```

5. **Setup environment variables**
   - Create a `.env` file in the root directory of the project.
   - Add your API keys and other environment variables to the `.env` file. For example:
     ```env
     GROQ_API_KEY=your_groq_api_key
     ```

## Project Structure

- `src/`: Contains the main application code.
  - `crew/agents.py`: Defines the agents used for email personalization and ghostwriting.
  - `crew/tasks.py`: Defines the tasks for personalizing and ghostwriting emails.
  - `main.py`: Contains the core logic to read the CSV file, create tasks, and execute them using Crew.
- `input/`: Directory to save the uploaded CSV files.
- `output/`: Directory where the generated personalized emails will be saved.
- `app.py`: Streamlit application for uploading CSV files and triggering the email generation process.

## Usage

1. **Run the Streamlit app**
   ```sh
   streamlit run app.py
   ```

2. **Upload the CSV file**
   - Ensure the CSV file contains the following columns: `first_name`, `last_name`, `email`, `bio`, `last_conversation`.
   - Upload the CSV file using the file uploader in the Streamlit app.

3. **Generate Personalized Emails**
   - After uploading the file, click on the "Generate Output Files" button to start the email generation process.
   - The personalized emails will be saved in the `output` folder and can be viewed and downloaded directly from the app.

## Example CSV File

```csv
first_name,last_name,email,bio,last_conversation
John,Doe,john.doe@example.com,"John is a software engineer with 5 years of experience.","Discussed project timelines."
Jane,Smith,jane.smith@example.com,"Jane is a marketing specialist with a knack for social media.","Talked about the new campaign."
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

