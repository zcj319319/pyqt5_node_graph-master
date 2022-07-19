module parent (
 input wire [3:0] cfg_of_son1,
 input wire [3:0] cfg_of_son2,
 input wire [3:0] cfg_of_son3,
 input wire   clk,
 input wire [10:0] din_of_son1_1,
 input wire [10:0] din_of_son1_2,
 input wire [10:0] din_of_son2,
 input wire   rst_n,
 output wire [15:0] dout_of_son3
);
wire [15:0] dout_of_son1_2;
wire [15:0] dout_of_son1_1;

SON1
U_SON1_1	(
	.cfg_of_son1		( cfg_of_son1		) ,
	.clk		( clk		) ,
	.din_of_son1		( din_of_son1_1		) ,
	.rst_n		( rst_n		) ,
	.dout_of_son1		( dout_of_son1_2		)
);


SON1
U_SON1_2	(
	.cfg_of_son1		( cfg_of_son1		) ,
	.clk		( clk		) ,
	.din_of_son1		( din_of_son1_2		) ,
	.rst_n		( rst_n		) ,
	.dout_of_son1		( dout_of_son1_1		)
);


SON2
U_SON2_1	(
	.cfg_of_son2		( cfg_of_son2		) ,
	.clk		( clk		) ,
	.din_of_son2		( din_of_son2		) ,
	.rst_n		( rst_n		) ,
	.dout_of_son2		( dout_of_son2		)
);


SON3
U_SON3_1	(
	.cfg_of_son3		( cfg_of_son3		) ,
	.clk		( clk		) ,
	.dout_of_son1_1		( dout_of_son1_1		) ,
	.dout_of_son1_2		( dout_of_son1_2		) ,
	.dout_of_son2		( dout_of_son2		) ,
	.rst_n		( rst_n		) ,
	.dout_of_son3		( dout_of_son3		)
);

endmodule