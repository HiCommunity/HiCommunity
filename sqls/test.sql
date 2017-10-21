### Run these SQL in your environment to initialize database TEST.

USE hicommunity;
INSERT INTO questions_region (name, address) VALUES ('Python', 'py');
INSERT INTO questions_region (name, address) VALUES ('数据库', 'db');
INSERT INTO questions_region (name, address) VALUES ('JavaScript', 'js');
INSERT INTO questions_region (name, address) VALUES ('Linux', 'linux');
INSERT INTO questions_region (name, address) VALUES ('娱乐', 'entertainment');

INSERT INTO questions_board(name, address, region_id) VALUES ('Django', 'django', 1);
INSERT INTO questions_board(name, address, region_id) VALUES ('Flask', 'flask', 1);
INSERT INTO questions_board(name, address, region_id) VALUES ('Tornado', 'tornado', 1);
INSERT INTO questions_board(name, address, region_id) VALUES ('爬虫', 'spider', 1);
INSERT INTO questions_board(name, address, region_id) VALUES ('机器学习', 'ml', 1);
INSERT INTO questions_board(name, address, region_id) VALUES ('大数据', 'big_data', 1);
INSERT INTO questions_board(name, address, region_id) VALUES ('MySQL', 'mysql', 2);
INSERT INTO questions_board(name, address, region_id) VALUES ('Oracle', 'oracle', 2);
INSERT INTO questions_board(name, address, region_id) VALUES ('JQuery', 'jquery', 3);
INSERT INTO questions_board(name, address, region_id) VALUES ('Canvas', 'canvas', 3);
INSERT INTO questions_board(name, address, region_id) VALUES ('RedHat', 'redhat', 4);
INSERT INTO questions_board(name, address, region_id) VALUES ('Ubuntu', 'ubuntu', 4);