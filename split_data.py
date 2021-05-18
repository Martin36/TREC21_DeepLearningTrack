import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def filter_tokens(tokens, verbose=False):
    if verbose:
        print('Length before: {}'.format(len(tokens)))
    # Remove special char tokens
    tokens = [token for token in tokens if token not in '...,?:;·|``()&\'\'\'s']
    
    # Remove the ending of tokens ending with ".\d"
    tokens = [re.sub(r'\.\d', '', token) for token in tokens]
    
    # Remove trailing dots
    tokens = [token.rstrip('.') for token in tokens]

    # Remove all empty and one letter tokens
    tokens = [token for token in tokens if not len(token) < 2]
    
    # Remove long words, which are most likely a concatination of several words
    word_max_length = 25
    tokens = [token for token in tokens if not len(token) > word_max_length]
    
    # Remove all nr tokens
    tokens = [token for token in tokens if not is_number(token)]
    
    # Remove math equations
    tokens = [token for token in tokens if not re.search(r'\^|·|π|\d+,\d+|\d\/|\+', token)]
    
    # Remove stopwords
    s_words = stopwords.words('english')
    tokens = [token for token in tokens if token not in s_words]
        
    # Split tokens where there is a dot between words
    new_tokens = []
    dot_regex = r'.{3,}\..'
    for token in tokens:
        if re.match(dot_regex, token):
            splitted_tokens = token.split('.')
            for s_token in splitted_tokens:
                new_tokens.append(s_token)
        else:
            new_tokens.append(token)
        
    tokens = new_tokens
    
    if verbose:
        print('Length after: {}'.format(len(tokens)))

    return tokens

test_tokens = ['science', '&', 'mathematics', 'physicsthe', 'hot', 'glowing', 'surfaces', 'of', 'stars', 'emit', 'energy', 'in', 'the', 'form', 'of', 'electromagnetic', 'radiation', '.', '?', 'it', 'is', 'a', 'good', 'approximation', 'to', 'assume', 'that', 'the', 'emissivity', 'e', 'is', 'equal', 'to', '1', 'for', 'these', 'surfaces', '.', 'find', 'the', 'radius', 'of', 'the', 'star', 'rigel', ',', 'the', 'bright', 'blue', 'star', 'in', 'the', 'constellation', 'orion', 'that', 'radiates', 'energy', 'at', 'a', 'rate', 'of', '2.7', 'x', '10^32', 'w', 'and', 'has', 'a', 'surface', 'temperature', 'of', '11,000', 'k.', 'assume', 'that', 'the', 'star', 'is', 'spherical', '.', 'use', 'σ', '=', '...', 'show', 'morefollow', '3', 'answersanswersrelevanceratingnewestoldestbest', 'answer', ':', 'stefan-boltzmann', 'law', 'states', 'that', 'the', 'energy', 'flux', 'by', 'radiation', 'is', 'proportional', 'to', 'the', 'forth', 'power', 'of', 'the', 'temperature', ':', 'q', '=', 'ε', '·', 'σ', '·', 't^4', 'the', 'total', 'energy', 'flux', 'at', 'a', 'spherical', 'surface', 'of', 'radius', 'r', 'is', 'q', '=', 'q·π·r²', '=', 'ε·σ·t^4·π·r²', 'hence', 'the', 'radius', 'is', 'r', '=', '√', '(', 'q', '/', '(', 'ε·σ·t^4·π', ')', ')', '=', '√', '(', '2.7x10+32', 'w', '/', '(', '1', '·', '5.67x10-8w/m²k^4', '·', '(', '1100k', ')', '^4', '·', 'π', ')', ')', '=', '3.22x10+13', 'msource', '(', 's', ')', ':', 'http', ':', '//en.wikipedia.org/wiki/stefan_bolt', '...', 'schmiso', '·', '1', 'decade', 'ago0', '18', 'commentschmiso', ',', 'you', 'forgot', 'a', '4', 'in', 'your', 'answer', '.', 'your', 'link', 'even', 'says', 'it', ':', 'l', '=', '4pi', '(', 'r^2', ')', 'sigma', '(', 't^4', ')', '.', 'using', 'l', ',', 'luminosity', ',', 'as', 'the', 'energy', 'in', 'this', 'problem', ',', 'you', 'can', 'find', 'the', 'radius', 'r', 'by', 'doing', 'sqrt', '(', 'l/', '(', '4pisigma', '(', 't^4', ')', ')', '.', 'hope', 'this', 'helps', 'everyone.caroline', '·', '4', 'years', 'ago4', '1', 'comment', '(', 'stefan-boltzmann', 'law', ')', 'l', '=', '4pi', '*', 'r^2', '*', 'sigma', '*', 't^4', 'solving', 'for', 'r', 'we', 'get', ':', '=', '>', 'r', '=', '(', '1/', '(', '2t^2', ')', ')', '*', 'sqrt', '(', 'l/', '(', 'pi', '*', 'sigma', ')', ')', 'plugging', 'in', 'your', 'values', 'you', 'should', 'get', ':', '=', '>', 'r', '=', '(', '1/', '(', '2', '(', '11,000k', ')', '^2', ')', ')', '*', 'sqrt', '(', '(', '2.7', '*', '10^32w', ')', '/', '(', 'pi', '*', '(', '5.67', '*', '10^-8', 'w/m^2k^4', ')', ')', ')', 'r', '=', '1.609', '*', '10^11', 'm', '?', '·', '3', 'years', 'ago0', '1', 'commentmaybe', 'you', 'would', 'like', 'to', 'learn', 'more', 'about', 'one', 'of', 'these', '?', 'want', 'to', 'build', 'a', 'free', 'website', '?', 'interested', 'in', 'dating', 'sites', '?', 'need', 'a', 'home', 'security', 'safe', '?', 'how', 'to', 'order', 'contacts', 'online', '?']
filter_tokens(test_tokens, True)