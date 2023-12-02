/**
 * @file gps_imu_fusion.cpp
 * @author Jiaxu Xiao
 * @brief 
 * @version 0.1
 * @date 2023-12-03
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include "eskf_flow.h"

int main(int argc, char **argv) {
    google::InitGoogleLogging(argv[0]);
    FLAGS_colorlogtostderr = true;
    FLAGS_alsologtostderr = true;

    if (argc != 3) {
        std::cout << "Please enter right command and parameters!" << std::endl;

        return -1;
    }

    std::string config_file_path(argv[1]);
    std::string data_file_path(argv[2]);

    ESKFFlow eskf_flow(config_file_path, data_file_path);

    //使用该函数时相当于只使用IMU位姿解算
//    eskf_flow.TestRun();//only predict

    eskf_flow.Run();

    return 0;
}
