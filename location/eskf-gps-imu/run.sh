cd bulid
cmake ..
make
cd
cd /home/xu/eskf-gps-imu
./bulid/gps_imu_fusion ./config/config.yaml ./data
cd
cd /home/xu/eskf-gps-imu
python display_path.py