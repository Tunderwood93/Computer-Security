static int t = 0x31337;

int sleep(int sec) {
	t += sec;
}

int time() {
	return t;
}
