# bookshelf-server

Server API for Bookshelf, smart bookmarking app.
Written in:

-Python :snake:
-Flask :sake:

## Getting started with :book: Bookshelf :book:

:construction: Both CLI and desktop clients are under construction. :construction:

To get started using Bookshelf you can interact with the API directly (using Postman etc.).

## Account creation

### Step 1: Create an account

Make sure to make a note of your Api key.

<img width="425" alt="Screenshot 2021-08-22 at 19 20 23" src="https://user-images.githubusercontent.com/76471929/130351733-b55b9e69-628f-4dae-8133-97c1ce01e702.png">

### Step 2: Set your bookmarks :bookmark:

Set URLs in the form <www.example.com>

<img width="425" alt="Screenshot 2021-08-22 at 19 21 26" src="https://user-images.githubusercontent.com/76471929/130351782-fcfa0030-e2c4-43c7-99b2-647085051554.png">

### Step 3(optional): Check bookmarks :bookmark:

If at any point you want to check your bookmarks, use vvv

<img width="425" alt="Screenshot 2021-08-22 at 19 22 01" src="https://user-images.githubusercontent.com/76471929/130351808-ac2f5e76-c9e6-4cc1-878a-fc3ceb6d2362.png">

## Browser setup

All examples are taken from Google Chrome, however the setup is similar for most major browsers.

### Step 1: Go to settings

<img width="425" alt="Screenshot 2021-08-22 at 19 27 49" src="https://user-images.githubusercontent.com/76471929/130351965-1c0d7a0e-348b-4fb8-99c5-d0a3940a32f3.png">

### Step 2: Under search engines, select 'Manage search engines'

<img width="425" alt="Screenshot 2021-08-22 at 19 28 23" src="https://user-images.githubusercontent.com/76471929/130351977-f2d392e9-c2c5-4af2-8aff-b3c51158988b.png">

### Step 3: Add a new search engine

<img width="425" alt="Screenshot 2021-08-22 at 19 28 39" src="https://user-images.githubusercontent.com/76471929/130351981-a9c809e8-297c-4da6-bf99-07aed40d2d55.png">

### Step 4: Create the new search engine

- Name is what you will see in the settings menu.
- Keyword is what you will preface your bookmark command with, it tells the browser that you want to use Bookshelf.
- Finally enter the URL as shown, https://bookshelf-server-api.herokuapp.com/search/<Your API key here>/%s. The final %s will be replaced by your bookmark command.
  
<img width="425" alt="Screenshot 2021-08-22 at 19 32 34" src="https://user-images.githubusercontent.com/76471929/130351990-c1532434-b0d5-4d7b-8f48-7a850c6b5e43.png">
