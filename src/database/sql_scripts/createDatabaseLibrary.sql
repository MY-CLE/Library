CREATE TABLE "public.books" (
	"bookID" serial,
	"rating" FLOAT,
	"book_name" varchar(255),
	"borrowed_status" BOOLEAN NOT NULL,
	"borrowed_counter" serial NOT NULL,
	"borrowed_date" DATE NOT NULL,
	"due_date" DATE NOT NULL,
	CONSTRAINT "books_pk" PRIMARY KEY ("bookID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.customer" (
	"userID" integer(255) NOT NULL,
	"customer_name" varchar(255) NOT NULL,
	"customer_firstName" varchar(255) NOT NULL,
	"customer_mail" varchar(255) NOT NULL,
	CONSTRAINT "customer_pk" PRIMARY KEY ("userID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.borrowed" (
	"borrowID" serial NOT NULL,
	"bookID" serial NOT NULL,
	"userID" integer NOT NULL,
	"due_date" DATE NOT NULL,
	CONSTRAINT "borrowed_pk" PRIMARY KEY ("borrowID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.removed" (
	"removedID" serial NOT NULL,
	"bookID" serial NOT NULL,
	"removed_date" serial NOT NULL,
	"removed_reason" serial(255) NOT NULL,
	CONSTRAINT "removed_pk" PRIMARY KEY ("removedID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.credentials" (
	"email" TEXT NOT NULL,
	"password" TEXT NOT NULL,
	"userID" integer NOT NULL,
	CONSTRAINT "credentials_pk" PRIMARY KEY ("email")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "books" ADD CONSTRAINT "books_fk0" FOREIGN KEY ("rating") REFERENCES ""("");
ALTER TABLE "books" ADD CONSTRAINT "books_fk1" FOREIGN KEY ("borrowed_counter") REFERENCES ""("");
ALTER TABLE "books" ADD CONSTRAINT "books_fk2" FOREIGN KEY ("due_date") REFERENCES "borrowed"("due_date");


ALTER TABLE "borrowed" ADD CONSTRAINT "borrowed_fk0" FOREIGN KEY ("bookID") REFERENCES "books"("bookID");
ALTER TABLE "borrowed" ADD CONSTRAINT "borrowed_fk1" FOREIGN KEY ("userID") REFERENCES "customer"("userID");

ALTER TABLE "removed" ADD CONSTRAINT "removed_fk0" FOREIGN KEY ("bookID") REFERENCES "books"("bookID");

ALTER TABLE "credentials" ADD CONSTRAINT "credentials_fk0" FOREIGN KEY ("email") REFERENCES "customer"("customer_mail");
ALTER TABLE "credentials" ADD CONSTRAINT "credentials_fk1" FOREIGN KEY ("userID") REFERENCES "customer"("userID");

