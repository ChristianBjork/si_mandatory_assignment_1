let gender_query = `CREATE TABLE IF NOT EXISTS gender (
    Id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Label TEXT NOT NULL
)`;
let user_query = `CREATE TABLE IF NOT EXISTS user (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
   	Email TEXT NOT NULL,
	Cpr TEXT NOT NULL,
    NemId TEXT NOT NULL,
    GenderId INTEGER NOT NULL,
	FOREIGN KEY (GenderId) REFERENCES gender(Id)
)`;
let password_query = `CREATE TABLE IF NOT EXISTS password (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
   	UserId INTEGER NOT NULL,
	Password TEXT NOT NULL,
    IsActive TEXT NOT NULL,
	FOREIGN KEY (UserId) REFERENCES user(Id)
)`;

db.run(query, (err) => {
    if (err) {
        console.log(err);
    }
});
db.close();