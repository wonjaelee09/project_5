Korean Movie recommender
Description
The goal of this project is to recommend Korean movies that have a similar story as a provided foreign movies by measuring the cosine distance.
 

Background
Parasite was a movie that was nominated for three awards at Golden Globe Awards, four awards at Academy awards including for best picture which was the first non-English language film in Academy Awards history to do so. Did you know that this movie, with record breaking international recognition is ranked 19th in terms of number of movie admissions? 

Also, have you heard of this movie called Ode to My father which is ranked 4th in terms of number of Admissions to watch the film? Considering it didn’t have any international recognition, I thought probably unlikely. So I wanted to essentially take this opportunity to share some amazing Korean films because I believe there are a lot of hidden gems that went practically unnoticed by the international audience

 
 
Data Used
IMDB Pages
box office example: https://www.boxofficemojo.com/year/2005/?area=KR&grossesOption=calendarGrosses
example Movie: https://www.boxofficemojo.com/release/rl386696449/weekend/
example pro: https://pro.imdb.com/title/tt0475783?ref_=mojo_rl_summary&rf=mojo_rl_summary

Tools Used
Data Cleaning, EDA, and Visualization: Pickle, Pandas, Numpy, Re, Spacy, Seaborn
Topic Modeling: Scikit-learn, Nltk, Tensorflow
Data Vis: Streamlit
 

 

Results and Conclusions
I performed Topic modeling as more of an aside from my recommendation to see what kind of Korean movies were in store to recommend. Interestingly 40% of the movies were about School gangs, 22% about Family, 18% about Army/Military, 13% Zombie Apocalypse, and 7% relationship.

My recommender also seems to be working. When I looked up the movie Saw, my recommender recommended a Korean movie memories of murder which is about two detectives trying to piece together clues to find the murderer, which is similar to jigsaw testing people to solve puzzles to save themselves. Also, when I looked up love actually, my recommender came up with soonjeong man hwa which are both romance movies where an older gentleman dates a much younger girl.


Future Works
There are many future works I can do to enhance my recommender. First is to expand the size of the movie data for better expansive, quality recommendations. Use a collaborative Filter. Right now, the huge downfall of my recommender is that it would recommend the same movie for anyone because it’s not user specific. Using a collaborative Filter with other features would enhance the experience and finally to expand the app with more capabilities that are tailored for the user.
