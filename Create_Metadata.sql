Create Database Metadata;

Use Metadata;


Create table Domain 
(
	DomainId INT NOT NULL,
	Description VARCHAR(55),
	CONSTRAINT PK_domain_id PRIMARY KEY (DomainId)
);


CREATE TABLE BusinessTerms
(
	BusTermId VARCHAR(15) NOT NULL,
	Business_Term VARCHAR(55),
	Term_Desciption VARCHAR(255),
	CONSTRAINT PK_BusinessTerm_id PRIMARY KEY (BusTermId)
);


CREATE TABLE DomainRelationship
(
	ParentId INT NOT NULL,
	ChildId INT NOT NULL
);




CREATE TABLE DomainTermsRelationship
(
	ChildId INT NOT NULL,
	BusTermId VARCHAR(15) NOT NULL,
	CONSTRAINT FK_DomainTermsRelationship_TermID FOREIGN KEY (BusTermId) REFERENCES BusinessTerms(BusTermId)
);

DROP TABLE TechnicalTerms;

CREATE TABLE TechnicalTerms
(
	TechTermId VARCHAR(15) NOT NULL,
	Database_Name VARCHAR(55) NOT NULL,
	Label VARCHAR(55) NOT NULL,
	Property VARCHAR(55),
	Type VARCHAR(55),
	isIndexed  VARCHAR(55),
	uniqueConstraint VARCHAR(55),
	existenceConstraint VARCHAR(55)
	CONSTRAINT PK_TechTermId PRIMARY KEY (TechTermId)
);


CREATE TABLE TechBusBridge
(
	Bridge_Id INT NOT NULL IDENTITY(1,1),
	TechTermId VARCHAR(15) NOT NULL,
	BusTermId VARCHAR(15) NOT NULL,
	CONSTRAINT FK_TechTermId FOREIGN KEY(TechTermId) REFERENCES TechnicalTerms(TechTermId),
	CONSTRAINT FK_BusTermId FOREIGN KEY(BusTermId) REFERENCES BusinessTerms(BusTermId),
);