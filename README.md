# Later
Do It Later

## What is Later
Do It Later is a simple web app to record things that need to be done later,
either by you, a script or some other human. Later only records things, how they
are processed is up to you.

## Examples
- You are at work, a co-worker tells you about an interesting video, you post the
link to Later "watch-later" list. A cron job picks it up, downloads the video, puts
it on your media server to watch it later in the evening.
- You are at a grocery store, you get an idea about creating a "do it later"
web app. You dump your idea into a Later "todo" list. A cron job parses the todo
item, transforms it into [orgmode todo item](https://orgmode.org/manual/TODO-Basics.html)
and populates it to your orgmode agenda view.

## How
Send a POST or GET call with `data` payload to `path/to/file` URI.
### Examples

``` sh
curl -X POST -F 'data=write a readme for Later' https://localhost/todo
```
