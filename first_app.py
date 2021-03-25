import pickle as pkl
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import linear_kernel

import warnings

warnings.filterwarnings('ignore')

st.markdown(' ## What type of movies do you like?')

#age =st.slider(key='Age', label="Age", min_value=1, max_value=100, step=1, value = 21)
#genre =


st.title('Korean Movie Recommender')




with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pkl.load(f)
with open('final_df.pkl', 'rb') as f:
    final_df = pkl.load(f)

sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

title = st.text_input("Enter movie")
warns = st.empty()


indices = pd.Series(final_df.index,
                   index=final_df['clean_title'])

idx = indices[title]
sim_scores = list(enumerate(sim_matrix[idx]))

sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
sim_scores = sim_scores[1:5000]
movie_indices = [i[0] for i in sim_scores]
df_rec = final_df.iloc[movie_indices]
df_rec2 = df_rec[(df_rec['Korean'] == 'y')]
df_rec3 = df_rec2[['clean_title', 'US', 'Page_URL', 'Korean']].copy()
st.write(df_rec3.head(5))

# st.write(final_df.iloc[movie_indices])


# def content_based_recommender(title, sim_scores=sim_matrix):
#     idx = indices[title]
#
#     sim_scores = list(enumerate(sim_matrix[idx]))
#
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
#
#     sim_scores = sim_scores[1:5]
#
#     movie_indices = [i[0] for i in sim_scores]
#
#     return fixed_df2['title'].iloc[movie_indices]
#
# content_based_recommender('Rules of Dating')





# left_column, right_column = st.beta_columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")
#
# expander = st.beta_expander("FAQ")
# expander.write("Here you could put in some really, really long explanations...")
#
#
# import time
#
# 'Starting a long computation...'
#
# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
#
# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
#
# '...and now we\'re done!'
