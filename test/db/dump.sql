BEGIN TRANSACTION;
CREATE TABLE module_catalog
                        (previous_name varchar(64) primary key,
                        instance_name varchar(64),
                        parent_name varchar(64));
CREATE TABLE module_detail
                        (id INTEGER not null primary key,
                        instance_name varchar(64),
                        module_name varchar(64),
                        register_type varchar(64),
                        port_name varchar(64),
                        high_param_name varchar(64),
                        low_param_name varchar(64),
                        port_name_width varchar(64));
INSERT INTO "module_detail" VALUES(1,'U_SON1_1','SON1','input','clk','1','0','1');
INSERT INTO "module_detail" VALUES(2,'U_SON1_1','SON1','input','rst_n','1','0','1');
INSERT INTO "module_detail" VALUES(3,'U_SON1_1','SON1','input','cfg_of_son1','4','0','4');
INSERT INTO "module_detail" VALUES(4,'U_SON1_1','SON1','input','din_of_son1','W_DIN','0','11');
INSERT INTO "module_detail" VALUES(5,'U_SON1_1','SON1','output','dout_of_son1','W_DOUT','0','15');
CREATE TABLE module_param
                                    (id INTEGER not null primary key,
                                    instance_name varchar(64),
                                    module_name varchar(64),
                                    parameter varchar(64),
                                    value varchar(64));
INSERT INTO "module_param" VALUES(1,'U_SON1_1','SON1','W_DIN','11');
INSERT INTO "module_param" VALUES(2,'U_SON1_1','SON1','W_DOUT','15');
CREATE TABLE module_version_order
                        (instance_name varchar(64) primary key,
                        version varchar(64),
                        order_rule varchar(64));
CREATE TABLE save_file
                        (id INTEGER not null primary key,
                        module_name varchar(64),
                        file_content text);
INSERT INTO "save_file" VALUES(1,'SON1','module SON1 #(
    parameter integer W_DIN  = 11 ,
	parameter integer W_DOUT = 15 
)
(
    input  wire                    clk          ,
	input  wire                    rst_n        ,
	input  wire  [3:0]             cfg_of_son1  ,
	input  wire  [W_DIN - 1:0]     din_of_son1  ,
	output wire  [W_DOUT - 1:0]    dout_of_son1 
);




endmodule');
CREATE TABLE table_detail
                        (id INTEGER not null primary key,
                        instance_name varchar(64),
                        instance_name_suffix varchar(64),
                        module_name varchar(64),
                        direct varchar(64),
                        register_type varchar(32),
                        port_name varchar(64),
                        port_name_width varchar(64),
                        net_name varchar(64),
                        net_name_width varchar(64),
                        status varchar(64),
                        operation_count INTEGER,
                        table_num INTEGER,
                        start_location varchar(64),
                        end_location varchar(64));
INSERT INTO "table_detail" VALUES(1,'U_SON1_1','U_SON1_1(SON1)','SON1','input','wire','clk','1',NULL,NULL,'Unconnected',NULL,2,NULL,NULL);
INSERT INTO "table_detail" VALUES(2,'U_SON1_1','U_SON1_1(SON1)','SON1','input','wire','rst_n','1',NULL,NULL,'Unconnected',NULL,2,NULL,NULL);
INSERT INTO "table_detail" VALUES(3,'U_SON1_1','U_SON1_1(SON1)','SON1','input','wire','cfg_of_son1','4',NULL,NULL,'Unconnected',NULL,2,NULL,NULL);
INSERT INTO "table_detail" VALUES(4,'U_SON1_1','U_SON1_1(SON1)','SON1','input','wire','din_of_son1','11',NULL,NULL,'Unconnected',NULL,2,NULL,NULL);
INSERT INTO "table_detail" VALUES(5,'U_SON1_1','U_SON1_1(SON1)','SON1','output','wire','dout_of_son1','15',NULL,NULL,'Unconnected',NULL,1,NULL,NULL);
COMMIT;
