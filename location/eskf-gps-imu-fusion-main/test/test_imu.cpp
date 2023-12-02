#include <iostream>

#include "imu_tool.h"

int main(int argc, char **argv) {
    if (argc != 2) {
        std::cout << "Please enter right command!" << std::endl;
        std::cout << "$ ./test_imu data_file_path" << std::endl;

        return -1;
    }

    std::vector<IMUData> imu_data_buff;

    IMUTool::ReadIMUData(std::string(argv[1]), imu_data_buff);

    for (int i = 0; i < imu_data_buff.size(); ++i) {
        std::cout << "\nindex: " << i << std::endl;
        std::cout << "time: " << std::to_string(imu_data_buff.at(i).time) << std::endl;
        std::cout << "ref_gyro: " << imu_data_buff.at(i).true_angle_velocity.transpose() << std::endl;
        std::cout << "gyro: " << imu_data_buff.at(i).angle_velocity.transpose() << std::endl;
        std::cout << "accel: " << imu_data_buff.at(i).linear_accel.transpose() << std::endl;
    }

    return 0;
}

