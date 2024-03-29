CREATE TABLE public.books (
	bookID serial,
	rating FLOAT,
	book_name varchar(255) NOT NULL,
	borrowed_status BOOLEAN NOT NULL,
	borrowed_counter integer NOT NULL,
	borrowed_date DATE NOT NULL,
	due_date DATE NOT NULL,
	CONSTRAINT books_pk PRIMARY KEY (bookID)
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.customer (
	userID serial NOT NULL,
	customer_name varchar(255) NOT NULL,
	customer_firstName varchar(255) NOT NULL,
	customer_mail varchar(255) NOT NULL UNIQUE,
	CONSTRAINT customer_pk PRIMARY KEY (userID)
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.borrowed (
	borrowID serial NOT NULL,
	bookID integer NOT NULL,
	userID integer NOT NULL,
	due_date DATE NOT NULL UNIQUE,
	CONSTRAINT borrowed_pk PRIMARY KEY (borrowID)
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.removed (
	removedID serial NOT NULL,
	bookID integer NOT NULL,
	removed_date DATE NOT NULL,
	removed_reason varchar(255) NOT NULL,
	CONSTRAINT removed_pk PRIMARY KEY (removedID)
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.credentials (
	email TEXT NOT NULL,
	password TEXT NOT NULL,
	userID integer NOT NULL,
	CONSTRAINT credentials_pk PRIMARY KEY (email)
) WITH (
  OIDS=FALSE
);



ALTER TABLE public.books ADD CONSTRAINT books_fk0 FOREIGN KEY (due_date) REFERENCES public.borrowed(due_date);


ALTER TABLE public.borrowed ADD CONSTRAINT borrowed_fk0 FOREIGN KEY (bookID) REFERENCES public.books(bookID);
ALTER TABLE public.borrowed ADD CONSTRAINT borrowed_fk1 FOREIGN KEY (userID) REFERENCES public.customer(userID);

ALTER TABLE public.removed ADD CONSTRAINT removed_fk0 FOREIGN KEY (bookID) REFERENCES public.books(bookID);

ALTER TABLE public.credentials ADD CONSTRAINT credentials_fk0 FOREIGN KEY (email) REFERENCES public.customer(customer_mail);
ALTER TABLE public.credentials ADD CONSTRAINT credentials_fk1 FOREIGN KEY (userID) REFERENCES public.customer(userID);





