-- PART 2
CREATE TABLE IF NOT EXISTS "part2_image" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(60) NOT NULL);

-- PART 4
CREATE TABLE IF NOT EXISTS "part4_storeuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "part4_storeuser_user_id_2bfab213" ON "part4_storeuser" ("user_id");

CREATE TABLE IF NOT EXISTS "part4_computer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(256) NOT NULL, "price" real NOT NULL, "cart_id" integer NULL REFERENCES "part4_cart" ("id") DEFERRABLE INITIALLY DEFERRED, "default" bool NOT NULL, "order_id" integer NULL REFERENCES "part4_order" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "part4_computer_cart_id_f3434d1c" ON "part4_computer" ("cart_id");
CREATE INDEX "part4_computer_order_id_7fa23434" ON "part4_computer" ("order_id");

CREATE TABLE IF NOT EXISTS "part4_cart" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_price" real NOT NULL, "store_user_id" integer NOT NULL REFERENCES "part4_storeuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "part4_cart_store_user_id_64d33b01" ON "part4_cart" ("store_user_id");

CREATE TABLE IF NOT EXISTS "part4_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_price" real NOT NULL, "store_user_id" integer NOT NULL REFERENCES "part4_storeuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "part4_order_store_user_id_19d96053" ON "part4_order" ("store_user_id");

CREATE TABLE IF NOT EXISTS "part4_computerspecs" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cpu_id" integer NOT NULL REFERENCES "part4_cpu" ("id") DEFERRABLE INITIALLY DEFERRED, "display_id" integer NOT NULL REFERENCES "part4_display" ("id") DEFERRABLE INITIALLY DEFERRED, "graphics_card_id" integer NOT NULL REFERENCES "part4_graphicscard" ("id") DEFERRABLE INITIALLY DEFERRED, "hard_drive_id" integer NOT NULL REFERENCES "part4_harddrive" ("id") DEFERRABLE INITIALLY DEFERRED, "os_id" integer NOT NULL REFERENCES "part4_os" ("id") DEFERRABLE INITIALLY DEFERRED, "ram_id" integer NOT NULL REFERENCES "part4_ram" ("id") DEFERRABLE INITIALLY DEFERRED, "sound_card_id" integer NOT NULL REFERENCES "part4_soundcard" ("id") DEFERRABLE INITIALLY DEFERRED, "computer_id" integer NOT NULL REFERENCES "part4_computer" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "part4_computerspecs_cpu_id_8dd2251a" ON "part4_computerspecs" ("cpu_id");
CREATE INDEX "part4_computerspecs_display_id_4bab3fdd" ON "part4_computerspecs" ("display_id");
CREATE INDEX "part4_computerspecs_graphics_card_id_606a0cd2" ON "part4_computerspecs" ("graphics_card_id");
CREATE INDEX "part4_computerspecs_hard_drive_id_73d12453" ON "part4_computerspecs" ("hard_drive_id");
CREATE INDEX "part4_computerspecs_os_id_a5bd6957" ON "part4_computerspecs" ("os_id");
CREATE INDEX "part4_computerspecs_ram_id_99fce67b" ON "part4_computerspecs" ("ram_id");
CREATE INDEX "part4_computerspecs_sound_card_id_dd6ae5ec" ON "part4_computerspecs" ("sound_card_id");
CREATE INDEX "part4_computerspecs_computer_id_ce98a382" ON "part4_computerspecs" ("computer_id");

CREATE TABLE IF NOT EXISTS "part4_cpu" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);
CREATE TABLE IF NOT EXISTS "part4_display" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);
CREATE TABLE IF NOT EXISTS "part4_graphicscard" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);
CREATE TABLE IF NOT EXISTS "part4_harddrive" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);
CREATE TABLE IF NOT EXISTS "part4_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);
CREATE TABLE IF NOT EXISTS "part4_os" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);
CREATE TABLE IF NOT EXISTS "part4_ram" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" real NOT NULL, "name" varchar(256) NOT NULL, "desc" varchar(256) NOT NULL);