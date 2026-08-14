import os
import pickle
import csv
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def authenticate_youtube():
    """Authenticate with YouTube API using OAuth 2.0"""
    creds = None
    
    # Load credentials if they exist
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If no credentials, create new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'youtube_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next time
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('youtube', 'v3', credentials=creds)

def search_youtube_videos(youtube, query, max_results=10):
    """Search for videos on YouTube"""
    request = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results,
        type='video',
        order='relevance'
    )
    
    response = request.execute()
    return response.get('items', [])

def get_video_stats(youtube, video_id):
    """Get statistics for a specific video"""
    request = youtube.videos().list(
        part='statistics,snippet',
        id=video_id
    )
    
    response = request.execute()
    if response['items']:
        item = response['items'][0]
        return {
            'video_id': video_id,
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'published_at': item['snippet']['publishedAt'],
            'views': int(item['statistics'].get('viewCount', 0)),
            'likes': int(item['statistics'].get('likeCount', 0)),
            'comments': int(item['statistics'].get('commentCount', 0))
        }
    return None

def collect_world_cup_data():
    """Collect YouTube data for World Cup 2026"""
    youtube = authenticate_youtube()
    
    # Search queries for World Cup content
    queries = [
        'World Cup 2026 USA',
        'USMNT World Cup 2026',
        'World Cup 2026 highlights',
        'World Cup 2026 goals',
        'World Cup 2026 matches'
    ]
    
    all_videos = []
    
    print("Searching for World Cup videos...")
    for query in queries:
        print(f"  Searching: {query}")
        videos = search_youtube_videos(youtube, query, max_results=10)
        
        for video in videos:
            video_id = video['id']['videoId']
            stats = get_video_stats(youtube, video_id)
            if stats:
                all_videos.append(stats)
                print(f"    Found: {stats['title'][:50]}... ({stats['views']} views)")
    
    # Save to CSV
    output_file = 'data/raw/youtube_videos.csv'
    if all_videos:
        keys = all_videos[0].keys()
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_videos)
        print(f"\nData saved to {output_file}")
        print(f"Total videos collected: {len(all_videos)}")
    else:
        print("No videos found")

if __name__ == '__main__':
    collect_world_cup_data()