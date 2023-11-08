"""API.py."""

from __future__ import print_function

import os

import googleapiclient.discovery
import googleapiclient.errors

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    number = 1
    results = []
    result_values = ""
    while result_values is not None and result_values != []:
        result = sheet.values().get(spreadsheetId=id,
                                    range=f"A{number}:A{number + 100}").execute()
        result_values = result.get('values', [])
        if result_values is not None:
            [results.append(x[0]) for x in result_values]
            number += 100
        else:
            break
    return results


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=link.split("list=")[1]
    )
    response = request.execute()
    results = []
    while "nextPageToken" in response.keys():
        if response is not None:
            for x in response["items"]:
                results.append("https://youtube.com/watch?v=" + x["contentDetails"]['videoId'])
            request = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=link.split("list=")[1],
                pageToken=response["nextPageToken"]
            )
            response = request.execute()
    for x in response["items"]:
        results.append("https://youtube.com/watch?v=" + x["contentDetails"]['videoId'])
    return results


if __name__ == '__main__':
    # print(get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json'))
    print(len(get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                      'AIzaSyB3Ba4jDC8csHk3lLy7oVobC9Ndkag-k1Y')))
