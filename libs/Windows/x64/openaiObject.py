from r_openai import OpenAI
import json

class openaiObject():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = self.create_client()

    def create_client(self):
        return OpenAI(
            api_key=self.api_key
        )
    
    def get_auth(self):
        '''
        Authenticate with OpenAI API
        '''
        self.client.models.list()
        print("Authentication successful")

    def get_completions(self, prompt, model, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop):
        '''
        Get text completions from OpenAI API
        '''
        response = self.client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=int(max_tokens),
            temperature=float(temperature),
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
        )
        
        result = response.choices[0].text
        
        return result
    
    def get_transcript(self, audio_file):
        '''
        Get text transcript from OpenAI API
        '''
        audio_ = open(audio_file, "rb")
        transcript = self.client.audio.transcriptions.create(model="whisper-1", file=audio_)
        print("Transcript: ", transcript)
        
        result = transcript.text.encode().decode('unicode_escape').encode('latin-1').decode('utf-8')
        
        return result
    
    def get_audio_translations(self, audio_file):
        '''
        Get audio translations from OpenAI API
        '''
        audio_ = open(audio_file, "rb")
        translation = self.client.audio.translations.create(model="whisper-1", file=audio_)

        result = translation.text.encode().decode('unicode_escape').encode('latin-1').decode('utf-8')
        
        return result
    
    def get_chat_completions(self, model, messages, temperature, n, stop, max_tokens, only_text=False):
        '''
        Get chat completions from OpenAI API
        '''
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            n=n,
            stop=stop,
            max_tokens=max_tokens
        )

        if only_text:
            response = response.choices[0].message.content
        else:
            response = self.completion_response_to_json(response)
        
        return response
    
    def completion_response_to_json(self, response):
        '''
        Convert completion response to JSON
        '''
        return json.dumps(response, default=lambda o: o.__dict__)