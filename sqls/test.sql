### Run these SQL in your environment to initialize database TEST.

USE hicommunity;
INSERT INTO posts_region (name, address) VALUES ('Python', 'py');
INSERT INTO posts_region (name, address) VALUES ('数据库', 'db');
INSERT INTO posts_region (name, address) VALUES ('JavaScript', 'js');
INSERT INTO posts_region (name, address) VALUES ('Linux', 'linux');
INSERT INTO posts_region (name, address) VALUES ('娱乐', 'entertainment');

INSERT INTO posts_board(name, address, region_id) VALUES ('Django', 'django', 1);
INSERT INTO posts_board(name, address, region_id) VALUES ('Flask', 'flask', 1);
INSERT INTO posts_board(name, address, region_id) VALUES ('机器学习', 'ml', 1);
INSERT INTO posts_board(name, address, region_id) VALUES ('MySQL', 'mysql', 2);
INSERT INTO posts_board(name, address, region_id) VALUES ('Oracle', 'oracle', 2);
INSERT INTO posts_board(name, address, region_id) VALUES ('JQuery', 'jquery', 3);
INSERT INTO posts_board(name, address, region_id) VALUES ('Canvas', 'canvas', 3);
INSERT INTO posts_board(name, address, region_id) VALUES ('RedHat', 'redhat', 4);
INSERT INTO posts_board(name, address, region_id) VALUES ('Ubuntu', 'ubuntu', 4);