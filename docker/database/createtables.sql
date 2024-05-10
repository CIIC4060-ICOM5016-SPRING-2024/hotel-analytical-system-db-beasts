create table if not exists client(clid serial primary key not null,
                                  fname varchar not null,
                                  lname varchar not null,
                                  age int not null,
                                  memberyear int not null);
alter sequence client_clid_seq restart with 401;

create table if not exists chains(chid serial primary key not null ,
                                  cname varchar not null,
                                  springmkup float not null,
                                  summermkup float not null,
                                  fallmkup float not null,
                                  wintermkup float not null);
alter sequence chains_chid_seq restart with 6;

create table if not exists roomdescription(rdid serial primary key not null,
                                           rname varchar not null,
                                           rtype varchar not null,
                                           capacity int not null,
                                           ishandicap boolean not null);
alter sequence roomdescription_rdid_seq restart with 63;

create table if not exists hotel(hid serial primary key not null,
                                 chid int references chains(chid) not null,
                                 hname varchar not null,
                                 hcity varchar not null);
alter sequence hotel_hid_seq restart with 41;

create table if not exists employee(eid serial primary key not null,
                                    hid int references hotel(hid) not null,
                                    fname varchar not null,
                                    lname varchar not null,
                                    age int not null,
                                    position varchar not null,
                                    salary float not null);
alter sequence employee_eid_seq restart with 201;

create table if not exists login(lid serial primary key not null,
                                 eid int references employee(eid) not null,
                                 username varchar not null unique,
                                 password varchar not null);
alter sequence login_lid_seq restart with 201;

create table if not exists room(rid serial primary key not null,
                                hid int references hotel(hid) not null,
                                rdid int references roomdescription(rdid) not null,
                                rprice float not null);
alter sequence room_rid_seq restart with 451;

create table if not exists roomunavailable(ruid serial primary key not null,
                                           rid int references room(rid) not null,
                                           startdate varchar not null,
                                           enddate varchar not null);
alter sequence roomunavailable_ruid_seq restart with 4999;

create table if not exists reserve(reid serial primary key not null,
                                   ruid int references roomunavailable(ruid) not null,
                                   clid int references client(clid) not null,
                                   total_cost float not null,
                                   payment varchar not null,
                                   guests int not null);
alter sequence reserve_reid_seq restart with 3801;