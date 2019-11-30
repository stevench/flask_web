"""empty message

Revision ID: 1c96bdc0a403
Revises: 4987f254d468
Create Date: 2019-11-30 14:20:51.003182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c96bdc0a403'
down_revision = '4987f254d468'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=256), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_user_username'), 'tb_user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_user_username'), table_name='tb_user')
    op.drop_table('tb_user')
    # ### end Alembic commands ###
