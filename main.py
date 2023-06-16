# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyboard

def transcribe_speech(language='en-US', file_path=None):
    # Initialize recognizer class
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Speak now...")

        try:
            # Set the language for speech recognition
            r.energy_threshold = 4000
            r.dynamic_energy_adjustment_ratio = 1.5
            r.pause_threshold = 0.8
            r.phrase_threshold = 0.3
            r.non_speaking_duration = 0.3
            r.operation_timeout = 5

            # listen for speech and store in audio_text variable
            audio_text = r.listen(source, phrase_time_limit=10)  # Set a time limit for each phrase

            st.info("Transcribing...")
            st.write("Press 'P' to pause or 'R' to resume")

            # Variables for pause and resume functionality
            paused = False
            resumed = False

            while not resumed:
                try:
                    # Check if user pressed 'P' to pause
                    if keyboard.is_pressed('p'):
                        paused = True
                        st.info("Paused. Press 'R' to resume")

                    if paused:
                        # Check if user pressed 'R' to resume
                        if keyboard.is_pressed('r'):
                            paused = False
                            resumed = True
                            st.info("Resumed. Continue speaking...")

                    if not paused:
                        # using Google Speech Recognition with the specified language
                        text = r.recognize_google(audio_text, language=language)
                        if file_path:
                            with open(file_path, 'w') as file:
                                file.write(text)
                            st.write("Transcribed text saved to file:", file_path)
                        return text

                except sr.UnknownValueError:
                    return "Sorry, I could not understand what you said."
                except sr.RequestError:
                    return "Sorry, there was an issue with the speech recognition service."

        except Exception as e:
            return "Sorry, there was an issue accessing the microphone: {}".format(e)









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import streamlit as st
    import speech_recognition as sr


    def main():
        st.title("Speech Recognition App")
        st.write("Click on the microphone to start speaking:")

        # add a button to trigger speech recognition
        if st.button("Start Recording"):
            file_path = "transcription.txt"  # Specify the desired file path
            language = st.text_input("Enter the language code (e.g., en-US for English (US)): ", value='en-US')
            text = transcribe_speech(language=language, file_path=file_path)
            st.write("Transcription:", text)


    if __name__ == "__main__":
        main()
