BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Teams";
CREATE TABLE IF NOT EXISTS "Teams" (
	"Id"	INTEGER,
	"Logo"	TEXT,
	"Name"	TEXT,
	"Sum"	INTEGER
);
DROP TABLE IF EXISTS "Category";
CREATE TABLE IF NOT EXISTS "Category" (
	"catcode"	INTEGER,
	"catname"	TEXT
);
DROP TABLE IF EXISTS "settings";
CREATE TABLE IF NOT EXISTS "settings" (
	"NameGame"	TEXT,
	"NumTheme"	INTEGER,
	"NumQue"	INTEGER,
	"TimeSec"	INTEGER,
	"Pad"	INTEGER,
	"tmpDat"	INTEGER,
	"tmpDat1"	INTEGER,
	"curCatCode"	INTEGER,
	"curCatName"	TEXT
);
DROP TABLE IF EXISTS "ThemeAndQ";
CREATE TABLE IF NOT EXISTS "ThemeAndQ" (
	"Theme"	TEXT,
	"Question"	TEXT,
	"Cost"	INTEGER,
	"Image"	TEXT,
	"Answer"	TEXT,
	"ImageA"	TEXT,
	"ToolTip"	TEXT,
	"ToolCost"	INTEGER,
	"IsBonus"	INTEGER,
	"ToolTipImg"	TEXT,
	"AnswerFin"	TEXT,
	"Catkod"	INTEGER,
	"Catname"	TEXT,
	"MMF"	TEXT,
	"TMMF"	TEXT
);
DROP TABLE IF EXISTS "steps";
CREATE TABLE IF NOT EXISTS "steps" (
	"cell_num"	INT
);
COMMIT;
