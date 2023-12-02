/**
 * @file imu_data.h
 * @author Jiaxu Xiao
 * @brief 
 * @version 0.1
 * @date 2023-12-03
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#ifndef GPS_IMU_FUSION_IMU_DATA_H
#define GPS_IMU_FUSION_IMU_DATA_H
#include <eigen3/Eigen/Core>
#include <eigen3/Eigen/Dense>
class IMUData {
public:
    IMUData() = default;

    double time = 0.0;
    Eigen::Vector3d linear_accel = Eigen::Vector3d::Zero();
    Eigen::Vector3d angle_velocity = Eigen::Vector3d::Zero();

    Eigen::Vector3d true_linear_accel = Eigen::Vector3d::Zero();
    Eigen::Vector3d true_angle_velocity = Eigen::Vector3d::Zero();

    Eigen::Quaterniond true_q_enu = Eigen::Quaterniond::Identity();
    Eigen::Vector3d true_t_enu = Eigen::Vector3d::Zero();
};

#endif //GPS_IMU_FUSION_IMU_DATA_H
