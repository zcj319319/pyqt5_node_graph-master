module wrapper();
video_system_wrapper inst_name
(
.aclk_0                        ()   ,//input          width:1
.aresetn_0                     ()   ,//input          width:1
.camera_rstn                   ()   ,//output         width:1
.din_0                         ()   ,//input          width:8
.en_capture_0                  ()   ,//input          width:1
.href_0                        ()   ,//input          width:1
.locked_0                      ()   ,//output         width:1
.m_axis_video_0_tdata          ()   ,//output         width:24
.m_axis_video_0_tlast          ()   ,//output         width:1
.m_axis_video_0_tready         ()   ,//input          width:1
.m_axis_video_0_tuser          ()   ,//output         width:1
.m_axis_video_0_tvalid         ()   ,//output         width:1
.overflow_0                    ()   ,//output         width:1
.pclk_0                        ()   ,//input          width:1
.s_axis_video_0_tdata          ()   ,//input          width:24
.s_axis_video_0_tlast          ()   ,//input          width:1
.s_axis_video_0_tready         ()   ,//output         width:1
.s_axis_video_0_tuser          ()   ,//input          width:1
.s_axis_video_0_tvalid         ()   ,//input          width:1
.status_0                      ()   ,//output         width:32
.underflow_0                   ()   ,//output         width:1
.vga_clk                       ()   ,//input          width:1
.vid_io_out_0_active_video     ()   ,//output         width:1
.vid_io_out_0_data             ()   ,//output         width:24
.vid_io_out_0_field            ()   ,//output         width:1
.vid_io_out_0_hblank           ()   ,//output         width:1
.vid_io_out_0_hsync            ()   ,//output         width:1
.vid_io_out_0_vblank           ()   ,//output         width:1
.vid_io_out_0_vsync            ()   ,//output         width:1
.vid_io_out_reset_0            ()   ,//input          width:1
.vsync_0                       ()   ,//input          width:1
.vtc_ctrl_araddr               ()   ,//input          width:9
.vtc_ctrl_arready              ()   ,//output         width:1
.vtc_ctrl_arvalid              ()   ,//input          width:1
.vtc_ctrl_awaddr               ()   ,//input          width:9
.vtc_ctrl_awready              ()   ,//output         width:1
.vtc_ctrl_awvalid              ()   ,//input          width:1
.vtc_ctrl_bready               ()   ,//input          width:1
.vtc_ctrl_bresp                ()   ,//output         width:2
.vtc_ctrl_bvalid               ()   ,//output         width:1
.vtc_ctrl_rdata                ()   ,//output         width:32
.vtc_ctrl_rready               ()   ,//input          width:1
.vtc_ctrl_rresp                ()   ,//output         width:2
.vtc_ctrl_rvalid               ()   ,//output         width:1
.vtc_ctrl_wdata                ()   ,//input          width:32
.vtc_ctrl_wready               ()   ,//output         width:1
.vtc_ctrl_wstrb                ()   ,//input          width:4
.vtc_ctrl_wvalid               ()   //input          width:1
);
endmodule

