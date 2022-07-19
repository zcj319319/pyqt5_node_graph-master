module rst_filter (
    ...
    );
    //端口声明...
    //wire定义...
    
   FUBS7T rst_n_ext_sync1_reg (.D(rst_n_ext),
       .Q(rst_n_ext_sync1),
       .T(clk));
   FUBS7T rst_n_ext_sync2_reg (.D(rst_n_ext_sync1),
       .Q(rst_n_ext_sync2),
       .T(clk));
   FUDS7T low_filter_cnt_reg_0_ (.D(n39),
       .Q(low_filter_cnt[0]),
       .R(por),
       .T(clk));
   V01S7T U3 (.A(low_filter_cnt[6]),
       .Y(n9));
   V01S7T U4 (.A(low_filter_cnt[4]),
       .Y(n15));
   AN3S7T U5 (.A(low_filter_cnt[0]),
       .B(low_filter_cnt[1]),
       .C(low_filter_cnt[2]),
       .Y(n41));
   N02S7T U6 (.A(n41),
       .B(low_filter_cnt[3]),
       .Y(n17));
   R02S7T U7 (.A(n15),
       .B(n17),
       .Y(n13));
   //...
endmodule