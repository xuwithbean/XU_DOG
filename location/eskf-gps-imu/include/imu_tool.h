/**
 * @file imu_tool.h
 * @author Jiaxu Xiao
 * @brief 
 * @version 0.1
 * @date 2023-12-03
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#ifndef GPS_IMU_FUSION_IMU_TOOL_H
#define GPS_IMU_FUSION_IMU_TOOL_H
#include "imu_data.h"
#include <vector>
#include <deque>
class IMUTool {
public:
    IMUTool() = default;

    static void ReadIMUData(const std::string &path,
                            std::vector<IMUData> &imu_data_buff,
                            const int skip_rows = 1);

    static void ReadIMUData(const std::string &path,
                            std::deque<IMUData> &imu_data_buff,
                            int skip_rows = 1);
};

#endif //GPS_IMU_FUSION_IMU_TOOL_H
