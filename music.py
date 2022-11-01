from base64 import decode
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Top Spotify Songs(2010-2019) EDA')
df = pd.read_csv('top10s.csv', encoding='latin1')

year_filter = st.slider('Year interval', 2010, 2019, 2019)
df_year = df[df['year'] <= year_filter]

new_df=df_year[['artist','title']].groupby('artist').count().reset_index()
df1=new_df.sort_values(by='title',ascending=False).head(10)

# draw the bar chart
fig, ax = plt.subplots()
pd.Series(list(df1.title), list(df1.artist)).plot.bar(ax=ax, color='orange').set_ylabel('Number of times on the list')
pd.Series(list(df1.title), list(df1.artist)).plot.bar(ax=ax, color='orange').set_title('Most Frequently Appeared Artist')

st.pyplot(fig)
# set the sidebar of Multiple Choice
singer_filter = st.sidebar.radio(
    "Choose a singer:",
    (df1['artist'].values[0], 
    df1['artist'].values[1], 
    df1['artist'].values[2],
    df1['artist'].values[3],
    df1['artist'].values[4],
    df1['artist'].values[5],
    df1['artist'].values[6],
    df1['artist'].values[7],
    df1['artist'].values[8],
    df1['artist'].values[9]))

st.subheader(f'{singer_filter}\'s creation trend')

#draw the line chart
fig2,ax = plt.subplots(nrows= 3,ncols=2,figsize=(15,7))
fig2.tight_layout(pad=3.0)    # Adjusting the space gap between the subplots
singer = df[df['artist']==singer_filter]
singer_bpm = singer.groupby(['year'],as_index=False)['bpm'].mean().apply(np.int64)      
#apply is used to make the floats to int
#mean_bpm                            
#by putting the as_index it removes the empty index and make bpm as a col name
singer_nrgy = singer.groupby(['year'],as_index=False)['nrgy'].mean().apply(np.int64)  
singer_dnce = singer.groupby(['year'],as_index=False)['dnce'].mean().apply(np.int64)  
singer_val = singer.groupby(['year'],as_index=False)['val'].mean().apply(np.int64)  
singer_dur = singer.groupby(['year'],as_index=False)['dur'].mean().apply(np.int64) 
singer_acous = singer.groupby(['year'],as_index=False)['acous'].mean().apply(np.int64)  

plt.style.use('Solarize_Light2')
ax[0][0].plot(singer_bpm['year'],singer_bpm['bpm'])
ax[0][0].set_title(f'Avg BPM from 2010 to {year_filter}')
ax[0][0].set_xlabel('Years')
ax[0][0].set_ylabel('BPM')

ax[0][1].plot(singer_nrgy['year'],singer_nrgy['nrgy'])
ax[0][1].set_title(f'Avg Energy level of the Songs from 2010 to {year_filter}')
ax[0][1].set_xlabel('Years')
ax[0][1].set_ylabel('Energy')

ax[1][0].plot(singer_dnce['year'],singer_dnce['dnce'])
ax[1][0].set_title(f'Avg Danceability from 2010 to {year_filter}')
ax[1][0].set_xlabel('Years')
ax[1][0].set_ylabel('dnce')

ax[1][1].plot(singer_val['year'],singer_val['val'])
ax[1][1].set_title(f'Avg Valence from 2010 to {year_filter}')
ax[1][1].set_xlabel('Years')
ax[1][1].set_ylabel('val')

ax[2][0].plot(singer_dur['year'],singer_dur['dur'])
ax[2][0].set_title(f'Avg Duration of the Songs from 2010 to {year_filter}')
ax[2][0].set_xlabel('Years')
ax[2][0].set_ylabel('dur')

ax[2][1].plot(singer_acous['year'],singer_acous['acous'])
ax[2][1].set_title(f'Avg Acoustic level from 2010 to {year_filter}')
ax[2][1].set_xlabel('Years')
ax[2][1].set_ylabel('acous')
st.pyplot(fig2)

# annotation
st.write('BPM : Beats Per Minute - The tempo of the song.')
st.write('Energy :  The energy of a song - the higher the value, the more energtic song.')
st.write('Danceability : the value denotes how easy it is to dance to this song.')
st.write('Valence : the value denotes how positive the mood of the song is.')
st.write('Duration : the value denotes the duration of the song in ms.')
st.write('Acousticness : the value denotes how acoustic the song is.')

st.subheader('Correlation between musical characteristics and popularity')

# draw the scatter chart1
fig3, ax = plt.subplots()
ax.scatter(x=df['nrgy'],y=df['pop'],c='orange')
ax.set_xlabel('nrgy')
ax.set_ylabel('pop')
ax.set_title('Song energy effect on popularity')
st.pyplot(fig3)

st.write('Judging from songs\' popularity score, 0.5-0.85 energy is a suitable window to set the energy level. ')

# draw the scatter chart2
fig4, ax = plt.subplots()
ax.scatter(x=df['dnce'],y=df['pop'],c='orange')
ax.set_xlabel('dnce')
ax.set_ylabel('pop')
ax.set_title('Song danceability effect on popularity')
st.pyplot(fig4)

st.write('Judging from songs\' popularity score, 0.55-0.85 danceability seems to be a good range to estimate a popular song would fall into. ')
