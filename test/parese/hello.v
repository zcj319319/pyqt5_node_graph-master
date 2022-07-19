module parent (
	clk ,
	rst_n ,
	cfg_of_son1 ,
	cfg_of_son2 ,
	cfg_of_son3 ,
	din_of_son2 ,
	din_of_son1_1 ,
	din_of_son1_2 ,
	dout_of_son3 ,
);
    input                                 clk                         ;
    input                                 rst_n                       ;
    input             [3:0]               cfg_of_son1                 ;
    input             [3:0]               cfg_of_son2                 ;
    input             [3:0]               cfg_of_son3                 ;
    input             [10:0]              din_of_son2                 ;
    input             [10:0]              din_of_son1_1               ;
    input             [10:0]              din_of_son1_2               ;
    output            [15:0]              dout_of_son3                ;

wire    [15:0]      dout_of_son1_1          ;       
wire    [15:0]      dout_of_son1_2          ;       

SON1
U_SON1_1	(
	.clk                           (clk	                           ) , 
	.rst_n                         (rst_n	                         ) , 
	.cfg_of_son1                   (cfg_of_son1	                   ) , 
	.din_of_son1                   (din_of_son1_2	                 ) , 
	.dout_of_son1                  (dout_of_son1_1	                )   
);


SON2
U_SON2_1	(
	.clk                           (clk	                           ) , 
	.rst_n                         (rst_n	                         ) , 
	.cfg_of_son2                   (cfg_of_son2	                   ) , 
	.din_of_son2                   (din_of_son2	                   ) , 
	.dout_of_son2                  (dout_of_son2	                  )   
);


SON1
U_SON1_2	(
	.clk                           (clk	                           ) , 
	.rst_n                         (rst_n	                         ) , 
	.cfg_of_son1                   (cfg_of_son1	                   ) , 
	.din_of_son1                   (din_of_son1_2	                 ) , 
	.dout_of_son1                  (dout_of_son1_2	                )   
);


SON3
U_SON3_1	(
	.clk                           (clk	                           ) , 
	.rst_n                         (rst_n	                         ) , 
	.cfg_of_son3                   (cfg_of_son3	                   ) , 
	.dout_of_son1_1                (dout_of_son1_1	                ) , 
	.dout_of_son1_2                (dout_of_son1_2	                ) , 
	.dout_of_son2                  (dout_of_son2	                  ) , 
	.dout_of_son3                  (dout_of_son3	                  )   
);

endmodule
