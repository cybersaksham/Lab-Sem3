class MaxHeap {
public:
	vector<long> v;
	
	void heapify(long i)
	{
		long l = this->left(i);
		long r = this->right(i);
		
		long largest = i;
		
		if (l < this->v.size() && this->v[l] > this->v[i]) largest = l;		
		if (r < v.size() && v[r] > v[largest]) largest = r;
		
		if (largest != i)
		{
			swap(this->v[i], this->v[largest]);
			this->heapify(largest);
		}
	}
	
	MaxHeap() { this->v = vector<long>(); }
	
	long parent(long i) const { return (i - 1) / 2; }
	
	long left(long i) const { return (2 * i + 1); }
	
	long right(long i) const { return (2 * i + 2); }
	
	bool isEmpty() const { return this->v.empty(); }
	
	long top() const
	{
		if (this->v.empty()) return -1;
		return this->v[0];
	}
	
	bool search(long x) const
	{
		for (long i : this->v)
		{
			if (i == x) return true;
		}
		return false;
	}
	
	void insert(long x)
	{
		this->v.push_back(x);
		
		long i = this->v.size() - 1;
		
		while (i > 0 && this->v[this->parent(i)] < this->v[i])
		{
			swap(this->v[i], this->v[this->parent(i)]);
			i = this->parent(i);
		}
	}
	
	void remove()
	{
		if(this->v.empty()) return;
		
		swap(this->v.front(), this->v.back());
		this->v.pop_back();
		
		this->heapify(0);
	}
};