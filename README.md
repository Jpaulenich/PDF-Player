PDF SPEED READER
A psychology-informed RSVP (Rapid Serial Visual Presentation) web tool
===============================================================

WHAT THIS SITE DOES
---------------------------------
Upload a PDF → extract the text → display words one-by-one at a chosen WPM with smart punctuation pauses.

WHY IT EXISTS
----------------------------
Most reading time isn't spent "understanding" words — it's spent *moving your eyes to find the next one*.
This tool reduces that wasted effort by keeping your eyes anchored to one point on the screen.


PSYCHOLOGY / HUMAN FACTORS
------------------------------------------

1) Fewer eye movements = less overhead
   Traditional reading forces constant saccades (eye jumps) + line resets.
   RSVP shows one word at a time in a fixed spot, so your eyes stay still.

2) Pivot-letter centering (ORP alignment)
   Instead of centering the whole word, the app centers a *pivot character* (red).
   Your brain recognizes words faster when your gaze lands near a consistent internal point.

3) Punctuation pauses improve comprehension
   Periods and commas naturally signal "meaning boundaries".
   Adding a tiny pause helps the brain chunk phrases into readable units instead of a nonstop stream.


CODING / SYSTEM DESIGN
-------------------------------------

Backend (Python Web Server)
- Accepts a PDF upload
- Extracts text (fast, local processing)
- Tokenizes into:
  - words
  - punctuation markers
- Sends tokens to the browser as JSON

Frontend (Browser Playback Engine)
- Runs a timing loop based on WPM:
    ms_per_word = 60000 / WPM
- Renders each token instantly with:
  - black background
  - white text
  - red pivot letter
- Adds extra delay when punctuation is encountered:
  - period pause slider
  - comma/other pause slider
- Controls:
  Play / Pause / Restart / Rewind / Forward + word counter (X/Y)


WHY THIS PROJECT MATTERS
------------------------
✓ Practical: a real reading tool you can tune to your brain  
✓ Technical: clean client/server split (extract once, play smoothly)  
✓ Design-focused: UI decisions are based on attention + perception, not aesthetics alone  


QUICK START
-----------
1) Upload a PDF (text-based PDFs work best)
2) Start at 250–350 WPM
3) Increase slowly
4) Tune punctuation pauses until it feels natural


LIMITATIONS
--------------------------
- Scanned PDFs may contain no selectable text (needs OCR)
- Complex layouts (columns/tables) may extract out of order
- Higher speed ≠ better comprehension for every document

===============================================================
