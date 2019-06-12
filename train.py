from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot(
    'Django ChatterBot Example',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            'response_selection_method': 'chatterbot.response_selection.get_first_response',
            'default_response': '我正在学习中',
            'maximum_similarity_threshold': 0.65
        }
    ],
    trainer='chatterbot.trainers.CorpusTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///online_bot_database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train( 'chatterbot.corpus.chinese' )