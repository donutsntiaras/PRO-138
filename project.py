# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:48:12 2022

@author: Vedgunika
"""

import pandas as pd
shared_articles = pd.read_csv('shared_articles.csv')
user_int = pd.read_csv("users_interactions.csv")
print(shared_articles.head(5))
print(user_int.head(5))

print(shared_articles.columns)
print(user_int.columns)

articles=shared_articles.merge(user_int,on='contentId')
print(articles.columns)

