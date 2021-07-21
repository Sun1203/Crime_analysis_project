drop table userjoin;

create table userjoin(
    userid varchar2(50),  --pk
    userpw varchar2(50) NOT NULL,
    username varchar2(50) NOT NULL,
    constraint pk_userjoin_userid primary key(userid)
);

