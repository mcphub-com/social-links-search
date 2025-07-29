import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/letscrape-6bRBa3QguO5/api/social-links-search'

mcp = FastMCP('social-links-search')

@mcp.tool()
def search_social_links(query: Annotated[str, Field(description='Social links search query.')],
                        social_networks: Annotated[Union[str, None], Field(description='Find social links for the specified social networks, specified as a comma delimited list of the following values: facebook, tiktok, instagram, snapchat, twitter, youtube, linkedin, github, pinterest. Default: facebook,tiktok,instagram,snapchat,twitter,youtube,linkedin,github')] = None) -> dict: 
    '''Get social profile links by search query or keywords. The following social networks are supported: Facebook, TikTok, Instagram, Snapchat, Twitter, Youtube, LinkedIn, GitHub and Pinterest.'''
    url = 'https://social-links-search.p.rapidapi.com/search-social-links'
    headers = {'x-rapidapi-host': 'social-links-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'social_networks': social_networks,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
