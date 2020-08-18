import speech_recognition as sr
import time
import os
import random
from PIL import Image

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    WORDS = ["beer", 'vodka', 'rum', 'alcohol', 'tequila', 'absinthe', 'draft', "wine"]
    bad_word = ['Seltzer', 'white']

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # format the instructions string
    instructions = (f'Tell me what you want is it a {WORDS}')
    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)
    print('So what will it be?')
    want = recognize_speech_from_mic(recognizer, microphone)

    if want["success"] and type(want['error']) != str:
        print('This is coming into first if')
        word_list = want['transcription'].split()
        for i in word_list:
            if i in WORDS:
                print(f"You may get a {i} good Sir!")
                path = random.choice(os.listdir("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\good\\"))
                print('This is the path: ', path)
                im = Image.open("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\good\\" + str(path))
                im.show()


            elif i in bad_word:
                print(f'You disgust me be gone!')
                path = random.choice(
                    os.listdir("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\bad\\"))
                print('This is the path: ', path)
                im = Image.open("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\bad\\" + str(path))
                im.show()


            else:
                print(f"You shall not have a beer! For you wanted {i}")
                path = random.choice(
                    os.listdir("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\confused\\"))
                print('This is the path: ', path)
                im = Image.open(
                    "C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\confused\\" + str(path))
                im.show()

    else:
        path = random.choice(os.listdir("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\error\\"))
        print('This is the path: ', path)
        im = Image.open("C:\\Users\Ferni\\Documents\\python_projects\\First_Project\\images\\error\\" + str(path))
        im.show()
        print("Could not hear you loser")
