import torch
from transformers import BertTokenizer
from transformers import BertTokenizer, BertModel


from model import *

class Predicter():
    def __init__(self):
        HIDDEN_DIM = 256
        OUTPUT_DIM = 1
        N_LAYERS = 2
        BIDIRECTIONAL = True
        DROPOUT = 0.25

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.bert = BertModel.from_pretrained('bert-base-uncased')


        self.model =  BERTGRUSentiment(self.bert,HIDDEN_DIM,OUTPUT_DIM,N_LAYERS,
                         BIDIRECTIONAL,DROPOUT)
        if torch.cuda.is_available() :
            self.model.load_state_dict(torch.load('checkpoint/tut6-model.pt'))
        else:
            self.model.load_state_dict(torch.load('checkpoint/tut6-model.pt',map_location='cpu'))

        self.model = self.model.to(self.device)
        
        
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.max_input_length = self.tokenizer.max_model_input_sizes['bert-base-uncased']

        self.init_token = self.tokenizer.cls_token
        self.eos_token = self.tokenizer.sep_token
        self.pad_token = self.tokenizer.pad_token
        self.unk_token = self.tokenizer.unk_token

        self.init_token_idx = self.tokenizer.convert_tokens_to_ids(self.init_token)
        self.eos_token_idx = self.tokenizer.convert_tokens_to_ids(self.eos_token)
        self.pad_token_idx = self.tokenizer.convert_tokens_to_ids(self.pad_token)
        self.unk_token_idx = self.tokenizer.convert_tokens_to_ids(self.unk_token)



    def predict_sentiment(self, sentence):
        self.model.eval()
        tokens = self.tokenizer.tokenize(sentence)
        tokens = tokens[:self.max_input_length-2]
        indexed = [self.init_token_idx] + self.tokenizer.convert_tokens_to_ids(tokens) + [self.eos_token_idx]
        tensor = torch.LongTensor(indexed).to(self.device)
        tensor = tensor.unsqueeze(0)
        prediction = torch.sigmoid(self.model(tensor))
        return prediction.item()


# pr = Predicter()
# print(pr.predict_sentiment('great work '))