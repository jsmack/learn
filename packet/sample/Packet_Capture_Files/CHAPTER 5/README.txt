�� CHAPTER 5 L4�v���g�R��
�� 5-01 UDP
- udp_header.pcapng
	UDP�w�b�_�[���m�F�ł���L���v�`���t�@�C��
- udp_firewall_accept.pcapng
	�t�@�C�A�E�H�[����UDP�f�[�^�O�����������Ă���Ƃ��̃L���v�`���t�@�C��
	PC�����M����UDP�f�[�^�O�����iNo.1�ANo.3�j���A�t�@�C�A�E�H�[���������A�T�[�o�[���烌�X�|���X���Ԃ��Ă��Ă���iNo.2�ANo.4�j
- udp_firewall_drop.pcapng
	�t�@�C�A�E�H�[����UDP�f�[�^�O�������h���b�v���Ă���Ƃ��̃L���v�`���t�@�C��
	PC�����M����UDP�f�[�^�O�������t�@�C�A�E�H�[�����h���b�v���Ă��邽�߁A�T�[�o�[���烌�X�|���X���Ȃ�
- udp_firewall_reject.pcapng
	�t�@�C�A�E�H�[����UDP�f�[�^�O���������ۂ��Ă���Ƃ��̃L���v�`���t�@�C��
	PC�����M����UDP�f�[�^�O�����i�No.�j���A�t�@�C�A�E�H�[�������ۂ��A�t�@�C�A�E�H�[������ICMP�p�P�b�g�iPort Unreachable�j���Ԃ��Ă��Ă���i����No.�j


�� 5-02 TCP
- tcp_header.pcapng
	TCP�w�b�_�[���m�F�ł���L���v�`���t�@�C��
- tcp_header_iphone_curl.pcapng
- tcp_header_iphone_safari.pcapng
- tcp_header_macosx_safari.pcapng
- tcp_header_ubuntu_curl.pcapng
- tcp_header_windows10_chrome.pcapng
- tcp_header_windows10_curl.pcapng
- tcp_header_windows10_edge.pcapng
- tcp_header_windows10_firefox.pcapng
	OS��Web�u���E�U�ɂ���ĈقȂ�TCP�w�b�_�[���m�F�ł���L���v�`���t�@�C��
- tcp_3whs_4wc.pcapng
	3�E�F�C�n���h�V�F�C�N�iNo.1�`No.3�j����A4�E�F�C�n���h�V�F�C�N�iNo.15�`No.18�j�܂ł̗�����m�F�ł���L���v�`���t�@�C��	
- tcp_stream_option.pcapng
	TCP�X�g���[���I�v�V�����ɂ���āA�G���[���������Ă���R�l�N�V�����𒊏o�ł���L���v�`���t�@�C��
- tcp_duplicate_ack.pcapng
	�d��ACK��Fast Retransmit�̓�����m�F�ł���L���v�`���t�@�C��
	No.11�Ɠ���ACK�p�P�b�g��No.13�ANo.15�ANo.17�ł��Ԃ��Ă��Ă���AFast Retransmit���������Ă���
- tcp_close_interruption.pcapng
	TCP�R�l�N�V������r���ŃL�����Z�������Ƃ��̃L���v�`���t�@�C��
	HTTP�Ńt�@�C�����_�E�����[�h���Ă���r���ŃL�����Z���������߁A�Ō��RST/ACK�p�P�b�g���Ԃ��Ă���iNo.733�j
- tcp_close_unavalable_service.pcapng
	�_�E�����Ă���T�[�r�X�ɑ΂��ăA�N�Z�X�����Ƃ��̃L���v�`���t�@�C��
	SYN�p�P�b�g��3�E�F�C�n���h�V�F�C�N�����݂���̂́i�No.�j�ARST/ACK�p�P�b�g�ŋ��ۂ���Ă���i����No.�j
- tcp_firewall_accept.pcapng
	�t�@�C�A�E�H�[����TCP�Z�O�����g�������Ă���Ƃ��̃L���v�`���t�@�C��
	PC�����M����TCP�Z�O�����g���A�t�@�C�A�E�H�[���������A�T�[�o�[���烌�X�|���X���Ԃ��Ă��Ă���
- tcp_firewall_reject.pcapng
	�t�@�C�A�E�H�[����TCP�Z�O�����g�����ۂ��Ă���Ƃ��̃L���v�`���t�@�C��
	PC�����M����TCP�Z�O�����g�iNo.1�j���A�t�@�C�A�E�H�[�������ۂ��A�T�[�o�[�i���ۂ̓t�@�C�A�E�H�[���j���烌�X�|���X���Ԃ��Ă��Ă���iNo.2�j
- tcp_firewall_drop.pcapng
	�t�@�C�A�E�H�[����TCP�Z�O�����g���h���b�v���Ă���Ƃ��̃L���v�`���t�@�C��
	PC�����M����TCP�Z�O�����g���t�@�C�A�E�H�[�����h���b�v���Ă��邽�߁A�T�[�o�[������t�@�C�A�E�H�[����������X�|���X���Ȃ�
- tcp_syn_retransmission.pcapng
	�T�[�o�[���牞�����Ȃ��ASYN���đ��M���Ă���Ƃ��̃L���v�`���t�@�C��
	�\���t�B���^�Ɂutcp.flags.syn eq 1�v����͂��A�����\���`�����u�O�ɕ\�����ꂽ�p�P�b�g����̕b���v�ɂ���ƁA�Ԋu��ς��Ȃ���ASYN���đ��M���Ă���
- tcp_delayed_ack.pcapng
	�x��ACK�̓�����m�F�ł���L���v�`���t�@�C��
	ACK�p�P�b�g�������i0.05�b�j�x��đ��M����Ă��邱�Ƃ�������iNo.3�ANo.6�ANo.9�ANo.12�j
- tcp_nagle_disable.pcapng
- tcp_nagle_enable.pcapng
	Nagle�A���S���Y����L���ɂ����Ƃ��A�����ɂ����Ƃ��̃L���v�`���t�@�C��
	Nagle�A���S���Y����L���ɂ��Ă���ƁAMSS�ɂ܂Ƃ߂đ��M���Ă���
	Nagle�A���S���Y���𖳌��ɂ��Ă���ƁAMSS�ɂȂ�O�ɂǂ�ǂ񑗐M���Ă���
- tcp_fast_open.pcapng
	Fast TCP Open�̓�����m�F�ł���L���v�`���t�@�C��
	�ŏ���3�E�F�C�n���h�V�F�C�N�iNo.1�`No.3�j��TCP Fast Open Cookie�����Ƃ肵�A2��ڂ�3�E�F�C�n���h�V�F�C�N�iNo.12�`No.14�j�ł�SYN����HTTP���b�Z�[�W�����Ƃ肵�Ă���
