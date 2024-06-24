import streamlit as st
import os
import pandas as pd
from src.main import crew_starter

# Function to save the uploaded file
def save_uploaded_file(uploadedfile, save_folder):
    try:
        file_path = os.path.join(save_folder, uploadedfile.name)
        with open(file_path, "wb") as f:
            f.write(uploadedfile.getbuffer())
        return file_path
    except Exception as e:
        print(e)
        return None

# Function to check for required columns
def check_required_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    return missing_columns

# Function to clear folder contents
def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                import shutil
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Main function for the Streamlit app
def main():
    st.title("Personalized Email Generator 📧")

    # Clear input and output folders if they are not empty
    input_folder = "input"
    output_folder = "output"
    if os.path.exists(input_folder):
        clear_folder(input_folder)
    if os.path.exists(output_folder):
        clear_folder(output_folder)

    # Display required columns message
    st.info("The following columns should be present in the CSV file before uploading: first_name, last_name, email, bio, last_conversation")

    # Create a folder to save the uploaded files if it doesn't exist
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file Of Email", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Check for required columns
        required_columns = ["first_name", "last_name", "email", "bio", "last_conversation"]
        missing_columns = check_required_columns(df, required_columns)

        if missing_columns:
            st.error(f"❌ The following required columns are missing: {', '.join(missing_columns)}")
        else:
            # Save the file if all required columns are present
            file_path = save_uploaded_file(uploaded_file, input_folder)
            if file_path:
                st.success(f"✅ File successfully Uploded")
                
                # Display the file content
                st.write("File Content:")
                st.dataframe(df)

                # Button to generate the output files
                if st.button("Generate Personalized Emails 🚀"):
                    with st.spinner("Generating response..."):
                        # Call the crew_starter function with the file path
                        crew_starter(file_path)

                    # Display and allow download of generated text files
                    st.success(f"✨ Personalized Email Are generated successfully")
                    for filename in os.listdir(output_folder):
                        if filename.endswith(".txt"):
                            with open(os.path.join(output_folder, filename), "r") as f:
                                st.write(f"Content of {filename}:")
                                st.text(f.read())
                            st.download_button(
                                label=f"Download {filename} ⬇️",
                                data=open(os.path.join(output_folder, filename), "rb").read(),
                                file_name=filename,
                                mime="text/plain"
                            )
                        st.info("NOTE: If it generates any error, try again by clicking on Generate Personalized Emails 🚀")
            else:
                st.error("❌ Failed to save file")

if __name__ == "__main__":
    main()
