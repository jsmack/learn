�� CHAPTER 3 L2�v���g�R��
�� 3-01 Ethernet
- ethernet_ethernet2.pcapng
	Ethernet�U�̃t���[���t�H�[�}�b�g���m�F�ł���L���v�`���t�@�C��
	HTTP��SMTP�ȂǁA��ʓI�ȃf�[�^�ʐM��Ethernet�U���g�p���Ă���
- ethernet_802.3.pcapng
	IEEE802.3�̃t���[���t�H�[�}�b�g���m�F�ł���L���v�`���t�@�C��
	CDP�iCisco Discovery Protocol�j��STP�iSpanning Tree Protocol�j��IEEE802.3���g�p���Ă���
- ethernet_broadcast.pcapng
	�u���[�h�L���X�g�ƃ��j�L���X�g�̃t���[�������邱�Ƃ��ł���L���v�`���t�@�C��
	Destination MAC�A�h���X���uff:ff:ff:ff:ff:ff�v�ɂȂ��Ă���iNo.1�j
- ethernet_802.1q.pcapng
	802.1q��VLAN2��VLAN�^�O���t�����p�P�b�g�����Ƃ肵�Ă���L���v�`���t�@�C��
	PC1�i10.2.2.101�j --- �i802.1q�j--- PC2�i10.2.2.102�j 
- ethernet_l2sw_pc1.pcapng
- ethernet_l2sw_pc2.pcapng
- ethernet_l2sw_pc3.pcapng
	L2�X�C�b�`�ɐڑ�����PC1�i192.168.1.1�j�APC2�i192.168.1.2�j�APC3�ł��ꂼ��擾�����L���v�`���t�@�C��
	PC1����PC2�ɑ΂���Ethernet�t���[���𑗐M����ƁAPC3�ɂ��t���b�f�B���O���ꂽ�p�P�b�g�����ł���
- ethernet_l2sw_mac-address table.txt
	L2�X�C�b�`�iCisco Catalyst�X�C�b�`�j��MAC�A�h���X�e�[�u���̏�Ԃ�\�����e�L�X�g�t�@�C��
- ethernet_l2loop_pc1.pcapng
- ethernet_l2loop_pc2.pcapng
	L2���[�v�����������Ƃ���PC�Ŏ擾�����L���v�`���t�@�C��
	�u���[�h�L���X�g���g�p���Ă���ARP Request�Ŗ��ߐs������Ă���


�� 3-02 PPPoE
- ppp_pap.cap
	PPP��PAP�F�؂����Ƃ��̃L���v�`���t�@�C��
	PAP�F�؂̓p�X���[�h���N���A�e�L�X�g�ŗ����iNo.5�`No.8�j
	# ���Ȃ݂ɁA�F�ؐ������OSPF�iOpen Shortest Path Fast�j�Ń��[�g�������Ƃ肵�Ă��� <--- OSPF�͖{���ł͎�舵���Ă��Ȃ�
- ppp_chap.cap
	PPP��CHAP�F�؂����Ƃ��̃L���v�`���t�@�C��
	CHAP�F�؂̓`�������W�l���g�p���āA�p�X���[�h���Í�������iNo.5�`No.10�j
	# ���Ȃ݂ɁA�F�ؐ������OSPF�iOpen Shortest Path Fast�j�Ń��[�g�������Ƃ肵�Ă��� <--- OSPF�͖{���ł͎�舵���Ă��Ȃ�
- pppoe.pcapng
	PPPoE�Őڑ������Ƃ��̃L���v�`���t�@�C��
	2�̃X�e�[�W���o�āiNo.1�`No.23�j�A���ۂ̃f�[�^�ʐM�Ɉڂ�iNo.24�ȍ~�j


�� 3-03 ARP
- arp_request_reply.pcapng
	�ł���ʓI��ARP Request��ARP Reply�̗����\���L���v�`���t�@�C��
	�u10.1.1.100�v����u10.1.1.200�v�ɑ΂���ICMP�p�P�b�g�𑗐M����O�ɁAARP�̂��Ƃ肪�s����
	PC1�i00:0c:29:ce:90:e4�j��ARP Request�Łu10.1.1.200�v��MAC�A�h���X���������悤�Ƃ���iNo.1�j
	PC2�i00:0c:29:5e:f5:ab�j��ARP Reply�ŉ�������iNo.2�j
- arp_ip_duplicated.pcapng
	PC1�i00:0c:29:ce:90:e4�j��PC2�i00:0c:29:5e:f5:ab�j�Ɠ���IP�A�h���X�u10.1.1.200�v���ݒ肳�ꂽ�Ƃ��̃L���v�`���t�@�C��
	PC1��IP�A�h���X���ݒ肳���Ɓu10.1.1.200�v��ARP Request���u���[�h�L���X�g�ő��M�����iNo.1�j
	����ɑ΂��āAPC2�����j�L���X�g��ARP Reply�ŉ�������iNo.2�j
