
# Library App — Run & Usage

This repository contains a simple library lookup app with a small Node.js backend and a static frontend.

## Prerequisites
- Node.js (includes `npm`) installed
- MongoDB running locally or a MongoDB Atlas URI

## Backend (in `backend/`)

1. Install dependencies (run in `cmd.exe` from the `backend` folder):

```cmd
cd backend
npm install
```

2. (Optional) Set environment variables in the same `cmd.exe` session if you need a remote DB:

```cmd
set MONGODB_URI=mongodb+srv://<user>:<password>@cluster0.mongodb.net
set DB_NAME=libraryDB
```

3. Seed the database (this clears and inserts sample books):

```cmd
npm run seed
```

4. Start the backend server:

```cmd
npm start
```

The server listens on `http://localhost:3000`.

## Frontend (in `frontend/`)

The frontend is static HTML/JS. Open `frontend/index.html` in your browser (double-click) or from `cmd.exe`:

```cmd
start "" "frontend\index.html"
```

Optional: serve the frontend on a local static server:

```cmd
npx http-server frontend -p 8080
```

Then open `http://localhost:8080`.

## API Endpoints (backend)

- `GET /books` — returns all books
- `GET /search?title=...` — search books by title (case-insensitive)
- `POST /addBook` — add a book (JSON body)
- `POST /deleteBook` — delete a book by id (JSON body with `id`)

### Example `curl` commands

Get all books:

```cmd
curl http://localhost:3000/books
```

Search for title containing "hobbit":

```cmd
curl "http://localhost:3000/search?title=hobbit"
```

Add a book:

```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"New Book\",\"author\":\"Me\"}" http://localhost:3000/addBook
```

Delete a book (replace `<OBJECT_ID>`):

```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"id\":\"<OBJECT_ID>\"}" http://localhost:3000/deleteBook
```

### Example JavaScript `fetch` (from the frontend)

```javascript
// get all books
fetch('/books')
	.then(r => r.json())
	.then(data => console.log(data));

// add a book
fetch('/addBook', {
	method: 'POST',
	headers: { 'Content-Type': 'application/json' },
	body: JSON.stringify({ title: 'My Book', author: 'Me' })
});
```

## Notes
- The backend code uses a simple Node `http` server and connects to MongoDB via `backend/db.js`.
- If you use a remote MongoDB, ensure network access and correct credentials.
- Environment variables set with `set` in `cmd.exe` only last for that session — start the server in the same window after setting them.

If you'd like, I can also:
- add a top-level `README.md` file (not inside the `README.md/` directory), or
- convert this content into a `README.md` at the project root — tell me which you prefer.

---
Updated run instructions and examples for the library app.
