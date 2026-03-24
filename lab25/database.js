const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const db = new sqlite3.Database(path.join(__dirname, 'database.db'));

db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL
    )
  `);

  db.get("SELECT COUNT(*) as count FROM users", (err, row) => {
    if (err) return;
    if (row.count === 0) {
      db.run("INSERT INTO users (name, email) VALUES (?, ?)", ['Іван Петренко', 'ivan@example.com']);
      db.run("INSERT INTO users (name, email) VALUES (?, ?)", ['Марія Шевченко', 'maria@example.com']);
    }
  });
});

module.exports = db;